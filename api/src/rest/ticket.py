from flask import Blueprint, request
from models.ticket import TicketSchema
from helpers.successResponse import successResponse
import data.ticket as ticketService

ticket = Blueprint('ticket', __name__)

@ticket.route('/', methods=['GET'])
def getTickets():
    schema = TicketSchema(many=True)
    return schema.dump(ticketService.getTickets())

@ticket.route('/', methods=['POST'])
def createTicket():
    schema = TicketSchema()
    ticket = schema.load(request.form)
    ticketService.createTicket(ticket)
    return successResponse()

@ticket.route('/<int:id>', methods=['GET'])
def getTicket(id):
    return 0

# @ticket.route('/<int:id>', methods=['PUT'])
# def updateTicket(id):
#     return 0

# @ticket.route('/<int:id>', methods=['DELETE'])
# def deleteTicket(id):
#     return 0

# @ticket.route('/<int:id>/block', method=['PUT'])
# def blockTicket(id):
#     return 0

# @ticket.route('/definitions', methods=['GET'])
# def getTicketDefinitions():
#     return json.dumps(ticketService.getTicketDefinitions(), cls=JsonExtendEncoder)
