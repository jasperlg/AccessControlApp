from data.database import fetchById, fetchOne
import bcrypt

GET_USER = '''
SELECT id, name, email, password_hash
FROM users
'''

def getUserById(id: int):
    return fetchById(GET_USER, id)

GET_USER_W_NAME = '''
SELECT id, name, password_hash
FROM users
WHERE name = %s
'''

def login(name: str, password: str):
    user = fetchOne(GET_USER_W_NAME, [name])
    
    if user is None:
        return None

    if bcrypt.checkpw(password.encode('utf-8'), user['password_hash'].encode('utf-8')):
        return user
    
    return None
