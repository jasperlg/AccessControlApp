from flask import Blueprint, request
from helpers.successResponse import successResponse
from models.bankAccount import BankAccountSchema
import data.bankAccount as bankAccountService

bankAccountBP = Blueprint('bankAccount', __name__)

@bankAccountBP.route('/', methods=['GET'])
def getBankAccounts():
    schema = BankAccountSchema(many=True)

    return schema.dumps(bankAccountService.getBankAccounts())

@bankAccountBP.route('/', methods=['POST'])
def createBankAccount():
    schema = BankAccountSchema()
    bankAccount = schema.load(request.form)
    bankAccountService.createBankAccount(bankAccount)

    return successResponse()

@bankAccountBP.route('/<int:id>', methods=['GET'])
def getBankAccount(id: int):
    schema = BankAccountSchema()

    return schema.dump(bankAccountService.getBankAccount(id))

@bankAccountBP.route('/<int:id>', methods=['PUT'])
def updateBankAccount(id: int):
    schema = BankAccountSchema()
    bankAccount = schema.load(request.form)
    bankAccountService.updateBankAccount(id, bankAccount)

    return successResponse()

@bankAccountBP.route('/<int:id>', methods=['DELETE'])
def deleteTicket(id: int):
    bankAccountService.deleteBankAccount(id)

    return successResponse()
