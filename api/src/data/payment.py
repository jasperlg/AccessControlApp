from models.payment import Payment
from data.database import fetchAll, fetchById, executeMany, execute

GET_PAYEMENTS = '''
SELECT id, ticket_id, payment_period, date, amount, payed_amount
FROM payments
'''

def getPayment(id: int):
    return fetchById(GET_PAYEMENTS, id)

GET_PAYEMENTS_OF_TICKET = '''
SELECT id, ticket_id, payment_period, date, amount, payed_amount
FROM payments
WHERE ticket_id = %s
'''

def getPaymentsOfTicket(ticket_id: int):
    return fetchAll(GET_PAYEMENTS_OF_TICKET, ticket_id)

CREATE_PAYEMENTS_OF_TICKET = '''
INSERT INTO payment (ticket_id, payment_period, date, amount)
VALUES
'''

def createPaymentsOfTicket(values: tuple[tuple]):
    executeMany(CREATE_PAYEMENTS_OF_TICKET, values, 4)

PAYEMENT_PAY = '''
UPDATE payment
SET payed_amount = payed_amount + %s, updated_at = now()
WHERE id = %s
'''

def payPayment(id: int, payed_amount: float):
    execute(PAYEMENT_PAY, (payed_amount, id))

SOFT_DELETE_PAYEMENT = '''
UPDATE payment
SET updated_at = now(), deleted_at = now()
WHERE id = %s
'''

def deletePayment(id: int):
    execute(SOFT_DELETE_PAYEMENT, [id])
