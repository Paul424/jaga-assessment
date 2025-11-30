import pytest
from unittest.mock import patch

from jaga.app import create_app
from jaga.db import db
from jaga.models.task import Task


@pytest.fixture
def app():
    #  Use a test database in memory for unittests
    app = create_app(
        config_override={
            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
            "SQLALCHEMY_TRACK_MODIFICATIONS": False,
        }
    )
    # Anything below the app fixture is within a simulated request
    with app.app_context():
        yield app


@pytest.fixture
def database(app):
    db.create_all()
    yield db
    db.session.remove()
    db.drop_all()


@pytest.fixture
def client(app, database):
    with app.test_client() as client:
        yield client


# For now initialize rows of data using a factory fixture (django style fixtures would be better)
@pytest.fixture
def task_factory():
    def _build(**data):
        t = Task(**data)
        db.session.add(t)
        db.session.commit()
        return t

    return _build


# Fixture to bypass oauth2 for views
@pytest.fixture()
def no_oauth():
    with patch(
        "jaga.auth.decorators.require_oauth.acquire_token", lambda scopes: scopes
    ):
        yield
