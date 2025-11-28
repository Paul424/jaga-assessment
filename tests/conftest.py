import pytest
from jaga.app import create_app
from jaga.db import db

@pytest.fixture
def app():
    #  Use a test database in memory for unittests
    app = create_app(config_override={
         "SQLALCHEMY_DATABASE_URI": 'sqlite:///:memory:',
         "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    })
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()
 
@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client
