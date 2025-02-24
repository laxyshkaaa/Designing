import datetime

from flask import Blueprint, jsonify, request, make_response

from db import get_connection
from error_response import create_error
from jwt_work import token_required, create_token

SignIn_blue = Blueprint('SignIn', __name__)

@SignIn_blue.route("/api/v1/SignIn", methods=['POST'])
def SignIn():
    conn = get_connection()
    cur = conn.cursor()

    user = request.get_json()
    email =user['corporative_email']
    input_password = user['password']

    cur.execute("select employee_id, password from employees where corporative_email = ?", (email,))
    result = cur.fetchone()
    if result:
        employee_id, stored_password = result

        if stored_password!= input_password:
            return jsonify((create_error("неверный пароль", 1009))), 403


        payload = {
            "sub" : str(employee_id),
            "exp" : datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }

        token = create_token(payload)

        response  = make_response({"token" : token})

        return response






