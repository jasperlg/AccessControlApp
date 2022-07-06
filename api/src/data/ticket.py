from models.ticket import Ticket
from data.database import fetch, insert

GET_TICKETS = '''
SELECT id, typeId, memberId, price, start_date, end_date, turns_left, active
FROM ticket
'''

def getTickets():
    return fetch(GET_TICKETS)

CREATE_TICKET = '''
INSERT INTO ticket (typeId, memberId, price, start_date, end_date, turns_left)
VALUES (%s, %s, %s, %s, %s, %s)
'''

def createTicket(ticket: Ticket):
    insert(CREATE_TICKET, (ticket.type_id, ticket.member_id, ticket.price, ticket.start_date, ticket.end_date, ticket.turns_left))

GET_TICKET_DEFINITIONS = '''
SELECT id, name, price, duration, turns, type
FROM ticket_definition
'''

def getTicketDefinitions():
    return fetch(GET_TICKET_DEFINITIONS)
