from flask import Blueprint, request
from helpers.authMiddleware import tokenRequired
from models.payement import PayementSchema, CreatePayementsSchema, PayPayementSchema
from helpers.successResponse import successResponse
import data.payement as payementService

payementBP = Blueprint('payement', __name__)

@payementBP.route('/payement/<int:id>', methods=['GET'])
@tokenRequired
def getPayement(id: int):
    schema = PayementSchema()
    
    return schema.dumps(payementService.getPayement(id))

@payementBP.route('/ticket/<int:ticket_id>/payement', methods=['GET'])
@tokenRequired
def getPayementsOfTicket(ticket_id: int):
    schema = PayementSchema(many=True)

    return schema.dumps(payementService.getPayementsOfTicket(ticket_id))

@payementBP.route('/ticket/<int:ticket_id>/payement/add', methods=['POST'])
@tokenRequired
def addPayementsOfTicket(ticket_id: int):
    payementsInput = request.form.to_dict()
    payementsInput['ticket_id'] = ticket_id

    schema = CreatePayementsSchema()
    newPayements = schema.load(payementsInput)

    payementService.createPayementsOfTicket(newPayements)

    return successResponse()

@payementBP.route('/payement/<int:id>/pay', methods=['PUT'])
@tokenRequired
def payPayement(id: int):
    schema = PayPayementSchema()
    payementInput = schema.load(request.form)

    payementService.payPayement(id, payementInput.payed_amount)

    return successResponse()

@payementBP.route('/payement/<int:id>', methods=['DELETE'])
@tokenRequired
def deletePayement(id: int):
    payementService.deletePayement(id)

    return successResponse()
