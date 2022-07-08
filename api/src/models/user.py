from typing_extensions import Self
from marshmallow import Schema, fields, post_load


class LoginUserSchema(Schema):
    name = fields.String(required=True)
    password = fields.String(required=True)
