import json
from helpers.JsonEncoder import JsonExtendEncoder

def successResponse():
    return json.dumps({ 'success': True })
