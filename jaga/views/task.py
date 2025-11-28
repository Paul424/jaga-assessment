from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy import desc, asc

from jaga.error import DataError
from jaga.db import db
from jaga.models.task import Task
from jaga.schemas.task import TaskSchema, PaginationQueryArgsSchema, OrderByFieldEnum, OperatorEnum

"""
REST view using flask_smorest / flask-rest-api (for clean views including validation) and marshmallow (for serialization)
"""

bp = Blueprint("tasks", "tasks", url_prefix="/tasks", description="Task operations")

@bp.route("/")
class TaskList(MethodView):
    @bp.arguments(PaginationQueryArgsSchema, location="querystring")
    @bp.response(200, TaskSchema(many=True))
    def get(self, args):
        # Build the query, run and return results
        q = db.select(Task)
        if "op" not in args:
            q = q.order_by(self._order_by_to_task_column(args.get("order_by")))
        elif args.get("op") == OperatorEnum.desc:
            q = q.order_by(desc(self._order_by_to_task_column(args.get("order_by"))))
        elif args.get("op") == OperatorEnum.asc:
            q = q.order_by(asc(self._order_by_to_task_column(args.get("order_by"))))
        else:
            raise DataError(f"Unexpected operator {args.get("op")} found")
        return db.paginate(q, page=args.get("page"), per_page=args.get("per_page"), max_per_page=10, error_out=False)

    @bp.arguments(TaskSchema)
    @bp.response(201, TaskSchema)
    def post(self, data):
        item = Task(**data)
        db.session.add(item)
        db.session.commit()
        return item
    
    @classmethod
    def _order_by_to_task_column(cls, order_by_enum):
        if order_by_enum == OrderByFieldEnum.id:
            return Task.id
        elif order_by_enum == OrderByFieldEnum.username:
            return Task.username
        elif order_by_enum == OrderByFieldEnum.email:
            return Task.email
        else:
            raise DataError(f"Unexpected order_by {order_by_enum} found")

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
