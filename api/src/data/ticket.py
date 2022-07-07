from models.ticket import Ticket
from data.database import fetchAll, fetchById, fetchOne, execute

GET_TICKETS = '''
SELECT id, type_id, member_id, price, start_date, end_date, turns_left, active
FROM ticket
'''

def getTickets():
    return fetchAll(GET_TICKETS)

def getTicket(id: int):
    return fetchById(GET_TICKETS, id)

GET_TICKET_W_TYPE = '''
SELECT t.id, t.type_id, t.member_id, t.price, t.start_date, t.end_date, t.turns_left, t.active, td.type
FROM ticket t
LEFT JOIN ticket_definition td ON t.type_id = td.id
WHERE t.id = %s
'''

def getTicketWithType(id: int):
    return fetchOne(GET_TICKET_W_TYPE, [id])

CREATE_TICKET = '''
INSERT INTO ticket (type_id, member_id, price, start_date, end_date, turns_left)
VALUES (%s, %s, %s, %s, %s, %s);
'''

def createTicket(ticket: Ticket):
    execute(CREATE_TICKET, (ticket.type_id, ticket.member_id, ticket.price, ticket.start_date, ticket.end_date, ticket.turns_left))

UPDATE_TICKET = '''
UPDATE ticket
SET type_id = %s, member_id = %s, price = %s, start_date = %s, end_date = %s, turns_left = %s, updated_at = now()
WHERE id = %s;
'''

def updateTicket(id: int, ticket: Ticket):
    execute(UPDATE_TICKET, (ticket.type_id, ticket.member_id, ticket.price, ticket.start_date, ticket.end_date, ticket.turns_left, id))

SOFT_DELETE_TICKET = '''
UPDATE ticket
SET updated_at = now(), deleted_at = now()
WHERE id = %s;
'''

def deleteTicket(id: int):
    execute(SOFT_DELETE_TICKET, [id])

BLOCK_TICKET = '''
UPDATE ticket
SET active = FALSE, updated_at = now()
WHERE id = %s;
'''

def blockTicket(id: int):
    execute(BLOCK_TICKET, [id])

USE_TICKET_TURN = '''
UPDATE ticket
SET turns_left = turns_left - 1, updated_at = now()
WHERE id = %s
'''

def useTicketTurn(id: int):
    execute(USE_TICKET_TURN, [id])

GET_TICKET_DEFINITIONS = '''
SELECT id, name, price, duration, turns, type
FROM ticket_definition;
'''

def getTicketDefinitions():
    return fetchAll(GET_TICKET_DEFINITIONS)
