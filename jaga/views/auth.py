from flask import Blueprint, url_for, redirect, session, request, jsonify, current_app

from jaga.auth.authlib import get_auth_client
from jaga.error import DataError
from jaga.auth.decorators import login_required
from jaga.models.auth import Token
from jaga.db import db

bp = Blueprint("auth", __name__, url_prefix="/auth")

"""
Views to support OAuth2 grant-type client-credentials, i.e. a human being access an endpoint which is a protected resource; these views 
are then used to negotiate with the upstream idp to eventually get a token.
"""


def create_or_update_token(token):
    """
    Store the token in the db; so we can validate the token from the header with the stored token
    """
    current_app.logger.debug(f"Create or update token using {token}")

    # Azure specific additional properties due to token_id (jwks)
    del token["ext_expires_in"]
    del token["id_token"]
    del token["expires_at"]
    del token["userinfo"]

    t = Token(**token)
    db.session.add(t)
    db.session.commit()


@bp.route("/token", methods=["GET"])
@login_required
def token():
    """
    View to generate an access-token. The token shall be used as a header in subsequent calls to the (REST) API
    Example:
        Authorization: Bearer a-token-string
    """
    access_token = session.get("access_token", None)
    if not access_token:
        raise DataError(f"Token not found in session")

    return jsonify(session["access_token"])


@bp.route("/login", methods=["GET"])
def login():
    auth_client = get_auth_client()

    # The local served authorize url (to which the client is redirected after login to the upstream idp)
    redirect_url = url_for("auth.authorize", _external=True)

    # Redirect to the upstream; providing the client-id, scope and our callback url
    return auth_client.authorize_redirect(redirect_url)


@bp.route("/authorize", methods=["GET"])
def authorize():
    """
    Idp redirects to this view inviting us to fetch the token and inject it in subsequent requests. For this simple test app we just
    store the token in the db so ResourceProtector can validate using the db.
    """
    auth_client = get_auth_client()

    # Fetch the token from the upstream (example: {'access_token': 'gho_xxxx', 'token_type': 'bearer', 'scope': 'user:email'})
    token = auth_client.authorize_access_token()

    # Store the token in the session
    session["access_token"] = token["access_token"]

    # Store the token in the db; we should expose only an id of the Token model
    create_or_update_token(token)

    # pop next
    next = request.args.get("next")

    # check for safe redirect url
    #

    return redirect(next or "/basic")


@bp.route("/logout", methods=["GET"])
def logout():
    # Pop the user info from the session
    session.pop("access_token", None)

    return redirect("/basic")


def register_views(app):
    app.register_blueprint(bp)
