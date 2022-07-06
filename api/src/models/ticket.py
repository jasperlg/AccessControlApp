from email.policy import default
from typing_extensions import Self
from marshmallow import Schema, fields, post_load

class Ticket:
    def __init__(self: Self, type_id, member_id, price, start_date, end_date, turns_left):
        self.type_id = type_id
        self.member_id = member_id
        self.price = price
        self.start_date = start_date
        self.end_date = end_date
        self.turns_left = turns_left

class TicketSchema(Schema):
    type_id = fields.Integer(required=True)
    member_id = fields.Integer(required=True)
    price = fields.Float(required=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    turns_left = fields.Integer(required=False, missing=None)

    @post_load
    def ticketInput(self: Self, data, **kwargs):
        return Ticket(**data)
