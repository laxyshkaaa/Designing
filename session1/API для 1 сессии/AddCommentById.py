import datetime

from flask import Blueprint, jsonify, request

from db import get_connection
from jwt_work import token_required

add_comment_blue = Blueprint('add_comment', __name__)

@add_comment_blue.route("/api/v1/Material/<int:material_id>/Comment", methods=['POST'])
@token_required

def add_comment(material_id, user_info):
    conn = get_connection()
    cur = conn.cursor()

    comment_data = request.get_json()
    text = comment_data['text']
    author_id = user_info.get('sub')





    query = """
   insert into comments (text, date_create, author_id)  OUTPUT INSERTED.comment_id values (?,?,?)

    """

    cur.execute(query, (text, datetime.datetime.now(), author_id))
    comment_id = cur.fetchone()[0]

    cur.execute('insert into comment_materials (material_id, comment_id) values (?,?)', (material_id, comment_id,))

    conn.commit()

    return jsonify({"comment_id" :comment_id })