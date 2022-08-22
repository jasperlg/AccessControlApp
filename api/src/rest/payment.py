from flask import Blueprint, request
from helpers.authMiddleware import tokenRequired
from models.payment import PaymentSchema, CreatePaymentsSchema, PayPaymentSchema
from helpers.successResponse import successResponse
import data.payment as PaymentService

paymentBP = Blueprint('payment', __name__)

@paymentBP.route('/payment/<int:id>', methods=['GET'])
@tokenRequired
def getPayment(id: int):
    schema = PaymentSchema()
    
    return schema.dumps(PaymentService.getPayment(id))

@paymentBP.route('/ticket/<int:ticket_id>/payment', methods=['GET'])
@tokenRequired
def getPaymentsOfTicket(ticket_id: int):
    schema = PaymentSchema(many=True)

    return schema.dumps(PaymentService.getPaymentsOfTicket(ticket_id))

@paymentBP.route('/ticket/<int:ticket_id>/payment/add', methods=['POST'])
@tokenRequired
def addPaymentsOfTicket(ticket_id: int):
    paymentsInput = request.form.to_dict()
    paymentsInput['ticket_id'] = ticket_id

    schema = CreatePaymentsSchema()
    newPayments = schema.load(paymentsInput)

    paymentService.createPaymentsOfTicket(newPayments)

    return successResponse()

@paymentBP.route('/payment/<int:id>/pay', methods=['PUT'])
@tokenRequired
def payPayment(id: int):
    schema = PayPaymentSchema()
    paymentInput = schema.load(request.form)

    paymentService.payPayment(id, paymentInput.payed_amount)

    return successResponse()

@paymentBP.route('/payment/<int:id>', methods=['DELETE'])
@tokenRequired
def deletePayment(id: int):
    paymentService.deletePayment(id)

    return successResponse()
