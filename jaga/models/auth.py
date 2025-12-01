from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from authlib.integrations.sqla_oauth2 import OAuth2TokenMixin

# Fetch the db instance
from jaga.db import db


class Token(db.Model, OAuth2TokenMixin):
    """
    Token model is required by authlib's ResourceProtector (validators) so we can validate access tokens in a clean way (from views perspective).

    The model however is not a good fit for Azure or icw jwt token, for now we make it fit but it would be better to define the oauth2 protocol first (grant-types, claim, scopes, ...) and then support the model for it.
    """
    id: Mapped[int] = mapped_column(primary_key=True)
    
    # Override to accommodate for Azure access_token (which are larger and cannot be indexed by postgresql)
    access_token = db.Column(String(4096), unique=False, nullable=False)
