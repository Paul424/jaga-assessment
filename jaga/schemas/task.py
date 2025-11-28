from marshmallow import Schema, fields

class TaskSchema(Schema):
    """
    Schema for the Task model for serialization and deserialization
    """
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
