from typing_extensions import Self

from marshmallow import Schema, fields, post_load


class BankAccount:
    def __init__(self: Self, id=None, member_id=None, account_number=None, holder_name=None, bank_name=None, iban=None, bic=None, mandate=None, mandate_date=None, domicile_number=None, sepa_status=None):      
        self.id = id
        self.member_id = member_id
        self.account_number = account_number
        self.holder_name = holder_name
        self.bank_name = bank_name
        self.iban = iban
        self.bic = bic
        self.mandate = mandate
        self.mandate_date = mandate_date
        self.domicile_number = domicile_number
        self.sepa_status = sepa_status

class BankAccountSchema(Schema):
    id = fields.Integer(dump_only=True)
    member_id = fields.Integer(required=True)
    account_number = fields.String(required=True)
    holder_name = fields.String(required=True)
    bank_name = fields.String(missing=None)
    iban = fields.String(required=True)
    bic = fields.String(required=True)
    mandate = fields.String(missing=None)
    mandate_date = fields.Date(missing=None)
    domicile_number = fields.String(missing=None)
    sepa_status = fields.String(missing=None)

    @post_load
    def bankAccountInput(self: Self, data, **kwargs):
        return BankAccount(member_id=data['member_id'], account_number=data['account_number'], holder_name=data['holder_name'], bank_name=data['bank_name'], iban=data['iban'], bic=data['bic'], mandate=data['mandate'], mandate_date=data['mandate_date'], domicile_number=data['domicile_number'], sepa_status=data['sepa_status'])
