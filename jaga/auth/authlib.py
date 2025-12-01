from flask import current_app
from authlib.integrations.flask_client import OAuth

from jaga.error import ConfigurationError


def get_auth_client():
    # fetch the oauth engine from the app
    auth_client = current_app.extensions.get("authlib.integrations.flask_client", None)
    if not auth_client:
        raise ConfigurationError(
            f"View requires the auth client but nothing seems registered on the app"
        )
    return getattr(auth_client, current_app.config["AUTH_NAME"])


def register_auth(app):
    app.logger.debug(f"Register Authlib")

    # The OAuth instance is registered as an app extension
    oauth = OAuth(app)

    # The concrete client itself is registered to the oauth instance
    _ = oauth.register(
        name=app.config["AUTH_NAME"],
        client_id=app.config["AUTH_CLIENT_ID"],
        client_secret=app.config["AUTH_CLIENT_SECRET"],
        access_token_url=app.config["AUTH_ACCESS_TOKEN_URL"],
        access_token_params=app.config["AUTH_ACCESS_TOKEN_PARAMS"],
        authorize_url=app.config["AUTH_AUTHORIZE_URL"],
        authorize_params=app.config["AUTH_AUTHORIZE_PARAMS"],
        api_base_url=app.config["AUTH_API_BASE_URL"],
        client_kwargs={
            "scope": app.config["AUTH_SCOPE"],
        },
        jwks_uri=app.config["AUTH_JWKS_URI"],
    )
