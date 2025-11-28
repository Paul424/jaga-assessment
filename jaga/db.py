from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import DeclarativeBase


# Using SQLAlchemy in declarative method
class Base(DeclarativeBase):
    pass


# The single SQLAlchemy instance
db = SQLAlchemy(model_class=Base)


def register_db(app):
    app.logger.debug(f"Register DB")

    # Register the db with the app
    db.init_app(app)

    # Register migration with the app
    migrate = Migrate(app, db)

    return db
