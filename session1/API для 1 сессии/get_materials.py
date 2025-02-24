from flask import Blueprint, jsonify

from db import get_connection
from jwt_work import token_required

get_matetials_blue = Blueprint('get_materials', __name__)

@get_matetials_blue.route("/api/v1/Materials", methods=['GET'])
@token_required

def get_materials(user_info):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("select material_id,title,  type_material, date_create from materials")

    materials = cur.fetchall()

    if materials:
        materials_json = []
        for mat in materials:
            materials_json.append({
                "id" : mat[0],
                "title": mat[1],
                "type": mat[2],
                "date": mat[3],
            })
        return jsonify(materials_json), 200