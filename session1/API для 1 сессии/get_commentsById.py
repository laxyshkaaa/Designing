from flask import Blueprint, jsonify

from db import get_connection
from jwt_work import token_required

get_comments_blue = Blueprint('get_comments', __name__)

@get_comments_blue.route("/api/v1/Material/<int:material_id>/Comments", methods=['GET'])
@token_required

def get_comments(material_id, user_info):
    conn = get_connection()
    cur = conn.cursor()

    query = """
   select c.comment_id, c.text, c.date_create, concat(e.last_name, ' ', e.first_name) as name, e.post
   from comments c
   inner join comment_materials cm on cm.comment_id = c.comment_id
   inner join employees e on e.employee_id = c.author_id
   where material_id = ? 
"""
    cur.execute(query, (material_id,))
    comments = cur.fetchall()

    if comments:
        comments_json = []
        for mat in comments:
            comments_json.append({
                "id" : mat[0],
                "text": mat[1],
                "date_create" : mat[2],
                "author": {
                    "name" : mat[3],
                    "post" : mat[4]
                }

            })
        return jsonify(comments_json), 200