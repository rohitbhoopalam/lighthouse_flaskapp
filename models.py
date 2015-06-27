from flaskext.mysql import MySQL
from app import mysql

connection = mysql.connect()

def get_top_questions(q_ref_id=None):
    cursor = connection.cursor()
    query = "SELECT * from Questions order by q_votes desc"
    if q_ref_id:
        query = "SELECT * from Questions where q_ref_id = '"+q_ref_id+"' order by q_votes desc"

    cursor.execute(query)

    data = cursor.fetchall()

    results = []

    for _d in data:
        print _d
        _data = {
            'q_id': _d[0],
            'q_question': _d[1],
            'q_ref_id': _d[2],
            'q_user_id': _d[3],
            'q_votes': _d[4],
            'q_state': _d[5]
            }
        results.append(_data)

    return results 

def insert_question(q_question, q_ref_id, q_user_id, q_votes=0, q_state=0):
    insert_query = """INSERT INTO Questions(q_question, q_ref_id, q_user_id, q_votes, q_state) \
        VALUES ("%s", "%s", "%s", %s, %s);""" % (q_question, q_ref_id, q_user_id, q_votes, q_state)

    cursor = connection.cursor()
    res = False
    try:
        res = cursor.execute(insert_query)
        connection.commit()
    except:
        connection.rollback()
    return res 

def upvote_question(q_id):
    update_query = """UPDATE Questions SET q_votes = q_votes + 1 where q_id = %s""" %q_id

    cursor = connection.cursor()
    res = False
    try:
        res = cursor.execute(update_query)
        connection.commit()
    except:
        connection.rollback()
    return res 

def get_top_answers(q_id):
    cursor = connection.cursor()
    query = "SELECT * from Answers order by a_votes desc"
    if q_id:
        query = "SELECT * from Answers where q_id = '" + q_id  + "'order by a_votes desc"

    cursor.execute(query)

    data = cursor.fetchall()

    results = []

    for _d in data:
        print _d
        _data = {
            'a_id': _d[0],
            'a_answer': _d[1],
            'q_id': _d[2],
            'a_user_id': _d[3],
            'a_votes': _d[4],
            'a_state': _d[5]
            }
        results.append(_data)

    return results 

def insert_answer(a_answer, q_id, a_user_id, a_votes=0, a_state=0):
    insert_query= """INSERT INTO Answers(a_answer, q_id, a_user_id, a_votes, a_state) \
        VALUES ("%s", "%s", "%s", %s, %s);""" % (a_answer, q_id, a_user_id, a_votes, a_state)

    cursor = connection.cursor()
    res = False
    try:
        res = cursor.execute(insert_query)
        connection.commit()
    except:
        connection.rollback()
    return res 

def upvote_answer(a_id):
    update_query = """UPDATE Answers SET a_votes = a_votes + 1 where a_id = %s""" %a_id

    cursor = connection.cursor()
    res = False
    try:
        res = cursor.execute(update_query)
        connection.commit()
    except:
        connection.rollback()
    return res 
