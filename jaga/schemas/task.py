from enum import Enum
from marshmallow import Schema, fields


class TaskSchema(Schema):
    """
    Schema for the Task model for serialization and deserialization
    """

    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)


class OrderByFieldEnum(Enum):
    id = 1
    username = 2
    email = 3


class OperatorEnum(Enum):
    desc = 1
    asc = 2


class PaginationQueryArgsSchema(Schema):
    """
    Schema for validating the page query parameter
    """

    page = fields.Int(load_default=1)
    per_page = fields.Int(load_default=10)
    order_by = fields.Enum(
        OrderByFieldEnum, by_value=False, load_default=OrderByFieldEnum.id
    )
    op = fields.Enum(OperatorEnum, by_value=False)
