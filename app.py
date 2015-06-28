from flask import Flask
from flaskext.mysql import MySQL
import json
from flask import jsonify
from flask import request 
from flask import Response
from crossdomain import crossdomain
 
mysql = MySQL()

app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'LightHouse'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

import models as m

@app.route('/questions')
@crossdomain(origin='*')
def get_questions():
    q_ref_id = request.args.get("q_ref_id", None)
    return Response(json.dumps(m.get_top_questions(q_ref_id=q_ref_id)),  mimetype='application/json')

@app.route('/insert_question', methods=["POST"])
@crossdomain(origin='*')
def insert_question():
    q_question = request.form.get("q_question", None)
    q_ref_id = request.form.get("q_ref_id", None)
    q_user_id = request.form.get("q_user_id", None)

    m.insert_question(q_question, q_ref_id, q_user_id)
    return Response(json.dumps(True),  mimetype='application/json')

@app.route('/upvote_question', methods=["GET", "POST"])
@crossdomain(origin='*')
def upvote_question():
    q_id = request.args.get("q_id", None)
    return Response(json.dumps(True),  mimetype='application/json')

@app.route('/answers')
@crossdomain(origin='*')
def get_answers():
    q_id = request.args.get("q_id", None)
    return Response(json.dumps(m.get_top_answers(q_id)),  mimetype='application/json')

@app.route('/insert_answer', methods=["POST"])
@crossdomain(origin='*')
def insert_answer():
    a_answer = request.form.get("a_answer", None)
    q_id = request.form.get("q_id", None)
    a_user_id = request.form.get("a_user_id", None)

    m.insert_answer(a_answer, q_id, a_user_id)
    return Response(json.dumps(True),  mimetype='application/json')

@app.route('/upvote_answer', methods=["POST"])
@crossdomain(origin='*')
def upvote_answer():
    a_id = request.form.get("a_id", None)
    m.upvote_answer(a_id)
    return Response(json.dumps(True),  mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True, port=8080)
