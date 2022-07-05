from crypt import methods
from flask import Blueprint
import data.tickets as ticketDB

ticket = Blueprint('ticket', __name__)

@ticket.route('/', methods=['GET'])
def getTickets():
    return ticketDB.get_ticket_definition()
