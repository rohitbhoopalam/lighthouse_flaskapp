from flask import Flask
from flaskext.mysql import MySQL
import json
from flask import jsonify
from flask import request 
 
mysql = MySQL()

app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'LightHouse'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

import models as m

@app.route('/questions')
def get_questions():
    q_ref_id = request.args.get("q_ref_id", None)
    return jsonify(data=m.get_top_questions(q_ref_id=q_ref_id))

@app.route('/insert_question', methods=["POST"])
def insert_question():
    q_question = request.form.get("q_question", None)
    q_ref_id = request.form.get("q_ref_id", None)
    q_user_id = request.form.get("q_user_id", None)

    if not (q_question and q_ref_id and q_user_id):
        return jsonify(result=False, error_msg="q_question, q_ref_id, q_user_id cannot be empty")

    if m.insert_question(q_question, q_ref_id, q_user_id):
        return jsonify(result=True)
    return jsonify(result=False, error_msg="Unknown error!!")

@app.route('/upvote_question', methods=["POST"])
def upvote_question():
    q_id = request.form.get("q_id", None)
    if not q_id:
        return jsonify(result=False, error_msg="q_id cannot be empty")

    if m.upvote_question(q_id):
        return jsonify(result=True)
    return jsonify(result=False, error_msg="Unknown error!!")

@app.route('/answers')
def get_answers():
    q_id = request.args.get("q_id", None)
    return jsonify(data=m.get_top_answers(q_id))

@app.route('/insert_answer', methods=["POST"])
def insert_answer():
    a_answer = request.form.get("a_answer", None)
    q_id = request.form.get("q_id", None)
    a_user_id = request.form.get("a_user_id", None)

    if not (a_answer and q_id and a_user_id):
        return jsonify(result=False, error_msg="a_answer, q_id, a_user_id cannot be empty")

    if m.insert_answer(a_answer, q_id, a_user_id):
        return jsonify(result=True)
    return jsonify(result=False, error_msg="Unknown error!!")

@app.route('/upvote_answer', methods=["POST"])
def upvote_answer():
    a_id = request.form.get("a_id", None)
    if not a_id:
        return jsonify(result=False, error_msg="a_id cannot be empty")

    if m.upvote_answer(a_id):
        return jsonify(result=True)
    return jsonify(result=False, error_msg="Unknown error!!")

if __name__ == '__main__':
    app.run(debug=True)
