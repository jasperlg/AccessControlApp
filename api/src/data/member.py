from models.member import Member
from data.database import fetchAll, fetchById, execute

GET_MEMBERS = '''
SELECT id, client_number, email, phone, name, rijksregister, gender, birth_date, street_and_number, city, postal_code
FROM member
'''

def getMembers():
    return fetchAll(GET_MEMBERS)

def getMember(id: int):
    return fetchById(GET_MEMBERS, id)

CREATE_MEMBER = '''
INSERT INTO member (client_number, email, phone, name, rijksregister, gender, birth_date, street_and_number, city, postal_code)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
'''

def createMember(member: Member):
    execute(CREATE_MEMBER, (member.client_number, member.email, member.phone, member.name, member.rijksregister, member.gender, member.birth_date, member.street_and_number, member.city, member.postal_code))

UPDATE_MEMBER = '''
UPDATE member
SET client_number = %s, email = %s, phone = %s, name = %s, rijksregister = %s, gender = %s, birth_date = %s, street_and_number = %s, city = %s, postal_code = %s, updated_at = now()
WHERE id = %s
'''

def updateMember(id: int, member: Member):
    execute(UPDATE_MEMBER, (member.client_number, member.email, member.phone, member.name, member.rijksregister, member.gender, member.birth_date, member.street_and_number, member.city, member.postal_code, id))

SOFT_DELETE_MEMBER = '''
UPDATE member
SET updated_at = now(), deleted_at = now()
WHERE id = %s
'''

def deleteMember(id: int):
    execute(SOFT_DELETE_MEMBER, [id])
