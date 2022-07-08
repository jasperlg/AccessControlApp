from flask import Blueprint, request
from helpers.authMiddleware import tokenRequired
from helpers.successResponse import successResponse
from models.bankAccount import BankAccountSchema
import data.bankAccount as bankAccountService

bankAccountBP = Blueprint('bankAccount', __name__)

@bankAccountBP.route('/', methods=['GET'])
@tokenRequired
def getBankAccounts():
    schema = BankAccountSchema(many=True)

    return schema.dumps(bankAccountService.getBankAccounts())

@bankAccountBP.route('/', methods=['POST'])
@tokenRequired
def createBankAccount():
    schema = BankAccountSchema()
    bankAccount = schema.load(request.form)
    bankAccountService.createBankAccount(bankAccount)

    return successResponse()

@bankAccountBP.route('/<int:id>', methods=['GET'])
@tokenRequired
def getBankAccount(id: int):
    schema = BankAccountSchema()

    return schema.dump(bankAccountService.getBankAccount(id))

@bankAccountBP.route('/<int:id>', methods=['PUT'])
@tokenRequired
def updateBankAccount(id: int):
    schema = BankAccountSchema()
    bankAccount = schema.load(request.form)
    bankAccountService.updateBankAccount(id, bankAccount)

    return successResponse()

@bankAccountBP.route('/<int:id>', methods=['DELETE'])
@tokenRequired
def deleteTicket(id: int):
    bankAccountService.deleteBankAccount(id)

    return successResponse()
