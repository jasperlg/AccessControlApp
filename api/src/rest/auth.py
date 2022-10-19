import json
from flask import Blueprint, Response, jsonify, request, abort
from flask_cors import CORS
import jwt
from config.config import getConfig
from models.user import LoginUserSchema
import data.user as userService

JWT_KEY = getConfig('AUTH')['JWT_KEY']

authBP = Blueprint('auth', __name__)

@authBP.route('/login', methods=['POST'])
def login():
    schema = LoginUserSchema()
    userInput = schema.load(request.json)
    
    user = userService.login(userInput['name'], userInput['password'])

    if user is None:
        abort(Response('Wrong name and password combination', 401))

    try:
        token = jwt.encode({'user_id': user['id']}, JWT_KEY, algorithm='HS256')

        return jsonify({'Authorization': token})
    except Exception as error:
        abort(Response('Error occured while generating token', error))
