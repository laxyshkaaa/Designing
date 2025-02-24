from functools import wraps

import jwt
from flask import request
secret = 'pavel'
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if token.startswith('Bearer '):
            token = token.split(' ')[1]

        decode_token = jwt.decode(token, secret, algorithms=['HS256'])

        return f(*args, **kwargs, user_info=decode_token)
    return decorated

def create_token(payload):
    return jwt.encode(payload, secret, algorithm='HS256')