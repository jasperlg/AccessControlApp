from typing_extensions import Self
from marshmallow import Schema, fields, post_load

SUBSCRIPTION = 'subscription'
TURN_CARD = 'turn_card'

class Ticket:
    def __init__(self: Self, id=None, type_id=None, member_id=None, price=None, start_date=None, end_date=None, turns_left=None, active=None):
        self.id = id
        self.type_id = type_id
        self.member_id = member_id
        self.price = price
        self.start_date = start_date
        self.end_date = end_date
        self.turns_left = turns_left
        self.active = active

class TicketSchema(Schema):
    id = fields.Integer(dump_only=True)
    type_id = fields.Integer(required=True)
    member_id = fields.Integer(required=True)
    price = fields.Float(required=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    turns_left = fields.Integer(missing=None)
    active = fields.Boolean(dump_only=True)

    @post_load
    def ticketInput(self: Self, data, **kwargs):
        return Ticket(type_id=data['type_id'], member_id=data['member_id'], price=data['price'], start_date=data['start_date'], end_date=data['end_date'], turns_left=data['turns_left'])

class TicketDefinition:
    def __init__(self: Self, id=None, type=None, name=None, price=None, duration=None, turns=None):
        self.id = id
        self.type = type
        self.name = name
        self.price = price
        self.duration = duration
        self.turns = turns

class TicketDefinitionSchema(Schema):
    id = fields.Integer(dump_only=True)
    type = fields.String(required=True)
    name = fields.String(required=True)
    price = fields.Float(required=True)
    duration = fields.String(missing=None)
    turns = fields.Integer(missing=None)
