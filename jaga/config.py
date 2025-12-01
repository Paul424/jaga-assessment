import os

SECRET_KEY = "!secret123"

# Server / domain
SERVER_NAME = os.getenv("SERVER_NAME", None)  # Set to match external domain

# Database
SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///jaga.db")

# Api
API_TITLE = "Jaga API"
API_VERSION = "v0.1.0"
OPENAPI_VERSION = "3.1.0"
OPENAPI_URL_PREFIX = "/"

# Auth Github
AUTH_NAME = os.getenv("AUTH_NAME", "github")
AUTH_CLIENT_ID = os.getenv(
    "AUTH_CLIENT_ID", "Ov23li3quIaI0ZJgR7Hy"
)  # default from github account
AUTH_CLIENT_SECRET = os.getenv(
    "AUTH_CLIENT_SECRET", "b5ec567487c60c083668f8bd6c9276fcbf28011c"
)  # default from github account
AUTH_ACCESS_TOKEN_URL = os.getenv(
    "AUTH_ACCESS_TOKEN_URL", "https://github.com/login/oauth/access_token"
)
AUTH_ACCESS_TOKEN_PARAMS = None
AUTH_AUTHORIZE_URL = os.getenv(
    "AUTH_AUTHORIZE_URL", "https://github.com/login/oauth/authorize"
)
AUTH_AUTHORIZE_PARAMS = None
AUTH_API_BASE_URL = os.getenv("AUTH_API_BASE_URL", "https://api.github.com/")
AUTH_SCOPE = os.getenv("AUTH_SCOPE", "user:email")
AUTH_JWKS_URI = os.getenv(
    "AUTH_JWKS_URI",
    None,
)

# Auth Azure
# AUTH_NAME = os.getenv("AUTH_NAME", "azure")
# AUTH_CLIENT_ID = os.getenv(
#     "AUTH_CLIENT_ID", "...."
# )
# AUTH_CLIENT_SECRET = os.getenv(
#     "AUTH_CLIENT_SECRET", "...."
# )
# AUTH_ACCESS_TOKEN_URL = os.getenv(
#     "AUTH_ACCESS_TOKEN_URL", "https://login.microsoftonline.com/804d6f85-9188-4618-ae1d-e387fe7fc33c/oauth2/v2.0/token"
# )
# AUTH_ACCESS_TOKEN_PARAMS = None
# AUTH_AUTHORIZE_URL = os.getenv(
#     "AUTH_AUTHORIZE_URL", "https://login.microsoftonline.com/804d6f85-9188-4618-ae1d-e387fe7fc33c/oauth2/v2.0/authorize",
# )
# AUTH_AUTHORIZE_PARAMS = None
# AUTH_API_BASE_URL = os.getenv("AUTH_API_BASE_URL", None)
# AUTH_SCOPE = os.getenv("AUTH_SCOPE", "openid profile email")
# AUTH_JWKS_URI = os.getenv(
#     "AUTH_JWKS_URI", "https://login.microsoftonline.com/804d6f85-9188-4618-ae1d-e387fe7fc33c/discovery/v2.0/keys",
# )
