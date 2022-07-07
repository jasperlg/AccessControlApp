from flask import Blueprint, request, abort, Response
from models.ticket import TicketSchema, TicketDefinitionSchema, TURN_CARD
from helpers.successResponse import successResponse
import data.ticket as ticketService

ticketBP = Blueprint('ticket', __name__)

@ticketBP.route('/', methods=['GET'])
def getTickets():
    schema = TicketSchema(many=True)

    return schema.dumps(ticketService.getTickets())

@ticketBP.route('/', methods=['POST'])
def createTicket():
    schema = TicketSchema()
    ticket = schema.load(request.form)
    ticketService.createTicket(ticket)

    return successResponse()

@ticketBP.route('/<int:id>', methods=['GET'])
def getTicket(id: int):
    schema = TicketSchema()

    return schema.dumps(ticketService.getTicket(id))

@ticketBP.route('/<int:id>', methods=['PUT'])
def updateTicket(id: int):   
    schema = TicketSchema()
    ticket = schema.load(request.form)
    ticketService.updateTicket(id, ticket)

    return successResponse()

@ticketBP.route('/<int:id>', methods=['DELETE'])
def deleteTicket(id: int):
    ticketService.deleteTicket(id)

    return successResponse()

@ticketBP.route('/<int:id>/block', methods=['PUT'])
def blockTicket(id: int):
    ticketService.blockTicket(id)

    return successResponse()

# TODO probably no id will be available
# TODO write code for opening gate
@ticketBP.route('/<int:id>/requestEntry', methods=['POST'])
def requestEntry(id: int):
    # check if ticket exists
    ticket = ticketService.getTicketWithType(id)
    
    # check if ticket is active
    if not ticket['active']:
        abort(Response('Ticket not active', 401))

    # check type
    print(ticket['type'] == TURN_CARD)
    if ticket['type'] == TURN_CARD:
        print(ticket['turns_left'])
        if ticket['turns_left'] > 0:
            ticketService.useTicketTurn(id)
        else:
            abort(Response('Ticket has no turns left', 401))

    return successResponse()

@ticketBP.route('/definitions', methods=['GET'])
def getTicketDefinitions():
    schema = TicketDefinitionSchema(many=True)

    return schema.dumps(ticketService.getTicketDefinitions())
