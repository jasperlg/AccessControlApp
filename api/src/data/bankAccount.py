from models.bankAccount import BankAccount
from data.database import fetchAll, fetchById, execute

GET_BANK_ACCOUNTS = '''
SELECT id, member_id, account_number, holder_name, bank_name, iban, bic, mandate, mandate_date, domicile_number, sepa_status
FROM bank_account
'''

def getBankAccounts():
    return fetchAll(GET_BANK_ACCOUNTS)

def getBankAccount(id: int):
    return fetchById(GET_BANK_ACCOUNTS, id)

CREATE_BANK_ACCOUNT = '''
INSERT INTO bank_account (member_id, account_number, holder_name, bank_name, iban, bic, mandate, mandate_date, domicile_number, sepa_status)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
'''

def createBankAccount(bankAccount: BankAccount):
    execute(CREATE_BANK_ACCOUNT, (bankAccount.member_id, bankAccount.account_number, bankAccount.holder_name, bankAccount.bank_name, bankAccount.iban, bankAccount.bic, bankAccount.mandate, bankAccount.mandate_date, bankAccount.domicile_number, bankAccount.sepa_status))

UPDATE_BANK_ACCOUNT = '''
UPDATE bank_account
SET member_id = %s, account_number = %s, holder_name = %s, bank_name = %s, iban = %s, bic = %s, mandate = %s, mandate_date = %s, domicile_number = %s, sepa_status = %s, updated_at = now()
WHERE id = %s;
'''

def updateBankAccount(id: int, bankAccount: BankAccount):
    execute(UPDATE_BANK_ACCOUNT, (bankAccount.member_id, bankAccount.account_number, bankAccount.holder_name, bankAccount.bank_name, bankAccount.iban, bankAccount.bic, bankAccount.mandate, bankAccount.mandate_date, bankAccount.domicile_number, bankAccount.sepa_status, id))

SOFT_DELETE_BANK_ACCOUNT = '''
UPDATE bank_account
SET updated_at = now(), deleted_at = now()
where id = %s;
'''

def deleteBankAccount(id: int):
    execute(SOFT_DELETE_BANK_ACCOUNT, [id])
