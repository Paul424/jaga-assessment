import os

SECRET_KEY = "!secret123"

# Database
SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///jaga.db")

# Api
API_TITLE = "Jaga API"
API_VERSION = "v0.1.0"
OPENAPI_VERSION = "3.1.0"
OPENAPI_URL_PREFIX = "/"

# Auth
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
