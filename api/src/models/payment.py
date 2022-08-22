from typing_extensions import Self
from marshmallow import Schema, fields, missing, post_load
from dateutil.relativedelta import relativedelta

class Payment:
    def __init__(self: Self, id=None, ticket_id=None, payment_period=None, date=None, amount=None, payed_amount=None):
        self.id = id
        self.ticket_id = ticket_id
        self.payment_period = payment_period
        self.date = date
        self.amount = amount
        self.payed_amount = payed_amount

class PaymentSchema(Schema):
    id = fields.Integer(dump_only=True)
    ticket_id = fields.Integer(required=True)
    payment_period = fields.Integer(missing=None)
    date = fields.Date(required=True)
    amount = fields.Float(required=True)
    payed_amount = fields.Float(required=True)        

    @post_load
    def paymentInput(self: Self, data, **kwargs):
        return Payment(ticket_id=data['ticket_id'], payment_period=data['payment_period'], date=data['date'], amount=data['amount'], payed_amount=data['payed_amount'])

class CreatePaymentsSchema(Schema):
    ticket_id = fields.Integer(required=True)
    payment_duration = fields.Integer(required=True)
    date_of_first_payment = fields.Date(required=True)
    amount = fields.Float(required=True)

    @post_load
    def createPaymentInput(self: Self, data, **kwargs):
        newData = []
        amountPerPayment = data['amount'] / data['payment_duration']

        for i in range(1, data['payment_duration'] + 1):
            newData.append((
                data['ticket_id'],
                i,
                data['date_of_first_payment'] + relativedelta(months=(i-1)),
                amountPerPayment
            ))
        
        return newData

class PayPaymentSchema(Schema):
    payed_amount = fields.Float(required=True)

    @post_load
    def paymentInput(self: Self, data, **kwargs):
        return Payment(payed_amount=data['payed_amount'])
