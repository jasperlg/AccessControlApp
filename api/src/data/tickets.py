from data.database import fetch

GET_TICKET_DEFINITION = '''
SELECT name, price, duration, turns, type
FROM ticket_definition
'''

def get_ticket_definition():
    allTickets = fetch(GET_TICKET_DEFINITION)
    print('ticket print')
    print(allTickets)
    return 'allTickets'
