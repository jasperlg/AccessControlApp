from data.database import doTransaction

members_insert = '''
INSERT INTO member (id, client_number, email, phone, name, rijksregister, gender, birth_date, street_and_number, city, postal_code)
VALUES
    (1, '1', 'jeff@email.com', '0412314324', 'Jef', '102334141', 'male', '1999-03-21', 'Straat 3', 'Stad', '100'),
    (2, '2', 'ben@email.com', '0412314324', 'Ben', '102334141', 'male', '1999-03-21', 'Straat 3', 'Stad', '100'),
    (3, '3', 'baard@email.com', '0412314324', 'Baard', '102334141', 'male', '1999-03-21', 'Straat 3', 'Stad', '100'),
    (4, '4', 'ann@email.com', '0412314324', 'Ann', '102334141', 'female', '1999-03-21', 'Straat 3', 'Stad', '100')
'''

bank_accounts_insert = '''
INSERT INTO bank_account (member_id, account_number, holder_name, bank_name, IBAN, BIC, mandate, mandate_date, domicile_number, SEPA_status)
VALUES
    (2, 'ewr32r234234', 'Ben', 'KBB', 'BE1245465463', '6702324234', 'dis is mandate', '2020-03-21', '12543534', 'goed')
'''

ticket_definitions_insert = '''
INSERT INTO ticket_definition (id, type, name, price, duration, turns)
VALUES
    (1, 'subscription', 'jaarabonnement', 496.3, '1 year', NULL),
    (2, 'turn_card', '10 beurtenkaart', 103.9, '2 year', 10)
'''

tickets_insert = '''
INSERT INTO ticket
VALUES (1, 1, 1, 496.3, '1999-07-03', '2000-07-03')
'''

# user with name = admin and password = 123456
users_insert = '''
INSERT INTO users (name, email, password_hash)
VALUES ('admin', 'admin@email.com', '$2b$12$uVIvVdv.YAAhWpv7haSSzeG1sbQYk0aNrGjV97VumVaIpPvBkuMhC')
'''

def seedDB():
    doTransaction(members_insert, bank_accounts_insert, ticket_definitions_insert, tickets_insert, users_insert)
