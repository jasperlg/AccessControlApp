from models.payement import Payement
from data.database import fetchAll, fetchById, executeMany, execute

GET_PAYEMENTS = '''
SELECT id, ticket_id, payement_period, date, amount, payed_amount
FROM payements
'''

def getPayement(id: int):
    return fetchById(GET_PAYEMENTS, id)

GET_PAYEMENTS_OF_TICKET = '''
SELECT id, ticket_id, payement_period, date, amount, payed_amount
FROM payements
WHERE ticket_id = %s
'''

def getPayementsOfTicket(ticket_id: int):
    return fetchAll(GET_PAYEMENTS_OF_TICKET, ticket_id)

CREATE_PAYEMENTS_OF_TICKET = '''
INSERT INTO payement (ticket_id, payement_period, date, amount)
VALUES
'''

def createPayementsOfTicket(values: tuple[tuple]):
    executeMany(CREATE_PAYEMENTS_OF_TICKET, values, 4)

PAYEMENT_PAY = '''
UPDATE payement
SET payed_amount = payed_amount + %s, updated_at = now()
WHERE id = %s
'''

def payPayement(id: int, payed_amount: float):
    execute(PAYEMENT_PAY, (payed_amount, id))

SOFT_DELETE_PAYEMENT = '''
UPDATE payement
SET updated_at = now(), deleted_at = now()
WHERE id = %s
'''

def deletePayement(id: int):
    execute(SOFT_DELETE_PAYEMENT, [id])
