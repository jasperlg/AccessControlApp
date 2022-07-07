from typing_extensions import Self
from marshmallow import Schema, fields, post_load


class Member:
    def __init__(self: Self, id=None, client_number=None, email=None, phone=None, name=None, rijksregister=None, gender=None, birth_date=None, street_and_number=None, city=None, postal_code=None):
        self.id= id
        self.client_number = client_number
        self.email = email
        self.phone = phone
        self.name = name
        self.rijksregister = rijksregister
        self.gender = gender
        self.birth_date = birth_date
        self.street_and_number = street_and_number
        self.city = city
        self.postal_code = postal_code

class MemberSchema(Schema):
    id = fields.Integer(dump_only=True)
    client_number = fields.String(missing=None)
    email = fields.Email(missing=None)
    phone = fields.String(missing=None)
    name = fields.String(required=True)
    rijksregister = fields.String(required=True)
    gender = fields.String(required=True)
    birth_date = fields.Date(required=True)
    street_and_number = fields.String(required=True)
    city = fields.String(required=True)
    postal_code = fields.String(required=True)

    @post_load
    def memberInput(self: Self, data, **kwargs):
        return Member(client_number=data['client_number'], email=data['email'], phone=data['phone'], name=data['name'], rijksregister=data['rijksregister'], gender=data['gender'], birth_date=data['birth_date'], street_and_number=data['street_and_number'], city=data['city'], postal_code=data['postal_code'])
