from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from authlib.integrations.sqla_oauth2 import OAuth2TokenMixin

# Fetch the db instance
from jaga.db import db


class Token(db.Model, OAuth2TokenMixin):
    id: Mapped[int] = mapped_column(primary_key=True)
