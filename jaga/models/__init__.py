from .task import *


def create_models(app, db):
    app.logger.debug(f"Create models")

    # Create the models
    with app.app_context():
        db.create_all()
