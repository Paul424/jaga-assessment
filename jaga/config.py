import os

SECRET_KEY = "!secret123"

# Database
SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///jaga.db")

# Api
API_TITLE = "Jaga API"
API_VERSION = "v0.1.0"
OPENAPI_VERSION = "3.1.0"
OPENAPI_URL_PREFIX = "/"

# Default config and overrides through environment variables
# ABC = os.getenv('ABC')
