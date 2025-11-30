from functools import wraps
from flask import current_app, request, redirect, url_for, session
from authlib.integrations.flask_oauth2 import ResourceProtector
from authlib.oauth2.rfc6750 import BearerTokenValidator
from authlib.oauth2.rfc7662 import IntrospectTokenValidator

from jaga.auth.authlib import get_auth_client
from jaga.models.auth import Token


def login_required(f):
    """
    Custom login-required decorator to test if the user is logged-in and redirect to the idp (oauth cycle) when this is not the case.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        current_app.logger.info(f"test if logged-in")
        # For now we just store the access-token in the session
        if not session.get("access_token"):
            auth_client = get_auth_client()

            # The local served authorize url (to which the client is redirected after login to the upstream idp)
            redirect_url = url_for("auth.authorize", next=request.url, _external=True)

            # Redirect to the upstream; providing the client-id, scope and our callback url
            return auth_client.authorize_redirect(redirect_url)

        return f(*args, **kwargs)
    return decorated_function


# Decorator to protect resources we own / expose
require_oauth = ResourceProtector()

class BearerTokenValidatorDb(BearerTokenValidator):
    """
    Validate token against stored in our db
    """
    def authenticate_token(self, token_string):
        current_app.logger.info(f"validate token using db")
        return Token.query.filter_by(access_token=token_string).first()

require_oauth.register_token_validator(BearerTokenValidatorDb())
