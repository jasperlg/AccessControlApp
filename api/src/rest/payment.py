from flask import Blueprint, request
from helpers.authMiddleware import tokenRequired
from models.payment import paymentSchema, CreatepaymentsSchema, PaypaymentSchema
from helpers.successResponse import successResponse
import data.payment as paymentService

paymentBP = Blueprint('payment', __name__)

@paymentBP.route('/payment/<int:id>', methods=['GET'])
@tokenRequired
def getpayment(id: int):
    schema = paymentSchema()
    
    return schema.dumps(paymentService.getpayment(id))

@paymentBP.route('/ticket/<int:ticket_id>/payment', methods=['GET'])
@tokenRequired
def getpaymentsOfTicket(ticket_id: int):
    schema = paymentSchema(many=True)

    return schema.dumps(paymentService.getpaymentsOfTicket(ticket_id))

@paymentBP.route('/ticket/<int:ticket_id>/payment/add', methods=['POST'])
@tokenRequired
def addpaymentsOfTicket(ticket_id: int):
    paymentsInput = request.form.to_dict()
    paymentsInput['ticket_id'] = ticket_id

    schema = CreatepaymentsSchema()
    newpayments = schema.load(paymentsInput)

    paymentService.createpaymentsOfTicket(newpayments)

    return successResponse()

@paymentBP.route('/payment/<int:id>/pay', methods=['PUT'])
@tokenRequired
def paypayment(id: int):
    schema = PaypaymentSchema()
    paymentInput = schema.load(request.form)

    paymentService.paypayment(id, paymentInput.payed_amount)

    return successResponse()

@paymentBP.route('/payment/<int:id>', methods=['DELETE'])
@tokenRequired
def deletepayment(id: int):
    paymentService.deletepayment(id)

    return successResponse()
