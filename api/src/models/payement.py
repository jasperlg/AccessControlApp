from typing_extensions import Self
from marshmallow import Schema, fields, missing, post_load
from dateutil.relativedelta import relativedelta

class Payement:
    def __init__(self: Self, id=None, ticket_id=None, payement_period=None, date=None, amount=None, payed_amount=None):
        self.id = id
        self.ticket_id = ticket_id
        self.payement_period = payement_period
        self.date = date
        self.amount = amount
        self.payed_amount = payed_amount

class PayementSchema(Schema):
    id = fields.Integer(dump_only=True)
    ticket_id = fields.Integer(required=True)
    payement_period = fields.Integer(missing=None)
    date = fields.Date(required=True)
    amount = fields.Float(required=True)
    payed_amount = fields.Float(required=True)        

    @post_load
    def payementInput(self: Self, data, **kwargs):
        return Payement(ticket_id=data['ticket_id'], payement_period=data['payement_period'], date=data['date'], amount=data['amount'], payed_amount=data['payed_amount'])

class CreatePayementsSchema(Schema):
    ticket_id = fields.Integer(required=True)
    payement_duration = fields.Integer(required=True)
    date_of_first_payement = fields.Date(required=True)
    amount = fields.Float(required=True)

    @post_load
    def createPayementInput(self: Self, data, **kwargs):
        newData = []
        amountPerPayement = data['amount'] / data['payement_duration']

        for i in range(1, data['payement_duration'] + 1):
            newData.append((
                data['ticket_id'],
                i,
                data['date_of_first_payement'] + relativedelta(months=(i-1)),
                amountPerPayement
            ))
        
        return newData

class PayPayementSchema(Schema):
    payed_amount = fields.Float(required=True)

    @post_load
    def payementInput(self: Self, data, **kwargs):
        return Payement(payed_amount=data['payed_amount'])
