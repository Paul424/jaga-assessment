from flask.views import MethodView
from flask_smorest import Blueprint, abort

from jaga.db import db
from jaga.models.task import Task
from jaga.schemas.task import TaskSchema

"""
REST view using flask_smorest / flask-rest-api (for clean views including validation) and marshmallow (for serialization)
"""

bp = Blueprint("tasks", "tasks", url_prefix="/tasks", description="Task operations")


@bp.route("/")
class TaskList(MethodView):
    @bp.response(200, TaskSchema(many=True))
    def get(self):
        # Query for items and return
        return Task.query.all()

    @bp.arguments(TaskSchema)
    @bp.response(201, TaskSchema)
    def post(self, data):
        item = Task(**data)
        db.session.add(item)
        db.session.commit()
        return item


@bp.route("/<int:task_id>")
class TaskDetail(MethodView):
    @bp.response(200, TaskSchema)
    def get(self, task_id):
        item = Task.query.get_or_404(task_id)
        return item

    @bp.arguments(TaskSchema)
    @bp.response(200, TaskSchema)
    def put(self, data, task_id):
        # Patch an existing item
        item = Task.query.get_or_404(task_id)
        item.username = data["username"]
        item.email = data["email"]
        db.session.commit()
        return item

    def delete(self, task_id):
        item = Task.query.get_or_404(task_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": f"item {task_id} deleted"}, 204


def register_views(api):
    api.register_blueprint(bp)
