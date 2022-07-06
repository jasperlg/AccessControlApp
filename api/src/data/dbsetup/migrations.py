from data.database import doTransaction

MEMBER = '''
CREATE TABLE IF NOT EXISTS member (
    id SERIAL PRIMARY KEY,
    client_number VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(255),
    name VARCHAR(255) NOT NULL,
    rijksregister VARCHAR(255) NOT NULL,
    gender VARCHAR(255) NOT NULL,
    birth_date DATE NOT NULL,
    street_and_number VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL,
    postal_code VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT now(),
    updated_at TIMESTAMP NOT NULL DEFAULT now(),
    deleted_at TIMESTAMP
)
'''

BANK_ACCOUNT = '''
CREATE TABLE IF NOT EXISTS bank_account (
    id SERIAL PRIMARY KEY,
    memberId INT NOT NULL,
    account_number VARCHAR(255) NOT NULL,
    holder_name VARCHAR(255) NOT NULL,
    bank_name VARCHAR(255),
    IBAN VARCHAR(255) NOT NULL,
    BIC VARCHAR(255) NOT NULL,
    mandate VARCHAR(255),
    mandate_date DATE,
    domicile_number VARCHAR(255),
    SEPA_status VARCHAR(255),
    FOREIGN KEY (memberId) REFERENCES member (id),
    created_at TIMESTAMP NOT NULL DEFAULT now(),
    updated_at TIMESTAMP NOT NULL DEFAULT now(),
    deleted_at TIMESTAMP
)
'''

TICKET_TYPE = '''
CREATE TYPE TICKET_TYPE AS ENUM ('subscription', 'turn_card')
'''

TICKET_DEFINITION = '''
CREATE TABLE IF NOT EXISTS ticket_definition (
    id SERIAL PRIMARY KEY,
    type TICKET_TYPE NOT NULL,
    name VARCHAR(255) NOT NULL,
    price FLOAT8 NOT NULL,
    duration INTERVAL,
    turns INT,
    created_at TIMESTAMP NOT NULL DEFAULT now(),
    updated_at TIMESTAMP NOT NULL DEFAULT now(),
    deleted_at TIMESTAMP
)
'''

TICKET = '''
CREATE TABLE IF NOT EXISTS ticket (
    id SERIAL PRIMARY KEY,
    typeId INT NOT NULL,
    memberId INT NOT NULL,
    price FLOAT8 NOT NULL,
    start_date DATE,
    end_date DATE,
    turns_left INT,
    active BOOLEAN NOT NULL DEFAULT TRUE,
    FOREIGN KEY (typeId) REFERENCES ticket_definition (id),
    FOREIGN KEY (memberId) REFERENCES member (id),
    created_at TIMESTAMP NOT NULL DEFAULT now(),
    updated_at TIMESTAMP NOT NULL DEFAULT now(),
    deleted_at TIMESTAMP
)
'''

PAYEMENT = '''
CREATE TABLE IF NOT EXISTS payement (
    id SERIAL PRIMARY KEY,
    ticketId INT NOT NULL,
    payement_period INT,
    date DATE NOT NULL,
    amount FLOAT8 NOT NULL,
    payed_amount FLOAT8 NOT NULL DEFAULT 0,
    FOREIGN KEY (ticketId) REFERENCES ticket (id),
    created_at TIMESTAMP NOT NULL DEFAULT now(),
    updated_at TIMESTAMP NOT NULL DEFAULT now(),
    deleted_at TIMESTAMP
)
'''

DROP_SCHEMA = '''
DROP TABLE IF EXISTS ticket, payement, ticket_definition, bank_account, member
'''

def removeDBTables():
    doTransaction(DROP_SCHEMA)

def createDBTables():
    try:
        doTransaction(TICKET_TYPE)
    except:
        print('TICKET_TYPE already exists')

    doTransaction(MEMBER, BANK_ACCOUNT, TICKET_DEFINITION, TICKET, PAYEMENT)
