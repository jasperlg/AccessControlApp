from functools import wraps
import jwt
from flask import request, abort, Response
from data.user import getUserById
from config.config import getConfig

JWT_KEY = getConfig('AUTH')['JWT_KEY']

def tokenRequired(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(' ')[1]
        if not token:
            abort(Response('Authentication Token is missing', 401))

        try:
            data = jwt.decode(token, JWT_KEY, algorithms=['HS256'])
            user = getUserById(data['user_id'])

            if user is None:
                abort(Response('Invalid Authentication Token', 401))

        except Exception as error:
            abort(Response(error, 500))

        # if needed the user can be passed on
        return func(*args, **kwargs)
    
    return decorated
