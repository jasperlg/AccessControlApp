import json

from flask import jsonify

def successResponse():
    return jsonify({ 'success': True })
