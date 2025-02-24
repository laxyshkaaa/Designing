from flask import Flask
from get_materials import get_matetials_blue
from get_commentsById import get_comments_blue
from AddCommentById import add_comment_blue
from SignIn import SignIn_blue
app = Flask(__name__)
app.config['secret'] = 'pavel'
app.register_blueprint(get_comments_blue)
app.register_blueprint(get_matetials_blue)
app.register_blueprint(add_comment_blue)
app.register_blueprint(SignIn_blue)


app.run(debug=True, port=7010)