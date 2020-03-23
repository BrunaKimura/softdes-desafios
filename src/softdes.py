# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 09:00:39 2017

@author: rauli
"""

import hashlib
import sqlite3
from datetime import datetime

from flask import Flask, request, render_template
from flask_httpauth import HTTPBasicAuth

DBNAME = './quiz.db'


def lambda_handler(event, context):
    try:
        import json
        import numbers

        def not_equals(first, second):
            if isinstance(first, numbers.Number) and isinstance(second, numbers.Number):
                return abs(first - second) > 1e-3
            return first != second

        ndes = int(event['ndes'])
        code = event['code']
        args = event['args']
        resp = event['resp']
        diag = event['diag']
        exec(code, locals())

        test = []
        for index, arg in enumerate(args):
            if not f'desafio{ndes}' in locals():
                return f"Nome da função inválido. Usar 'def desafio{ndes}(...)'"

            if not_equals(eval(f'desafio{ndes}(*arg)'), resp[index]):
                test.append(diag[index])

        return " ".join(test)
    except:
        return "Função inválida."


def convert_date(orig):
    return orig[8:10] + '/' + orig[5:7] + '/' + orig[0:4] + ' ' + orig[11:13] + ':' + orig[14:16] + ':' + orig[17:]


def get_quizes(user):
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    if user in ['admin', 'fabioja']:
        cursor.execute("SELECT id, numb from QUIZ".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    else:
        cursor.execute(
            "SELECT id, numb from QUIZ where release < '{0}'".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    info = [reg for reg in cursor.fetchall()]
    conn.close()
    return info


def get_user_quiz(userid, quizid):
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT sent,answer,result from USERQUIZ where userid = '{0}' and quizid = {1} order by sent desc".format(
            userid, quizid))
    info = [reg for reg in cursor.fetchall()]
    conn.close()
    return info


def set_user_quiz(userid, quizid, sent, answer, result):
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    # print("insert into USERQUIZ(userid,quizid,sent,answer,result) values ('{0}',{1},'{2}','{3}','{4}');".format(userid, quizid, sent, answer, result))
    # cursor.execute("insert into USERQUIZ(userid,quizid,sent,answer,result) values ('{0}',{1},'{2}','{3}','{4}');".format(userid, quizid, sent, answer, result))
    cursor.execute("insert into USERQUIZ(userid,quizid,sent,answer,result) values (?,?,?,?,?);",
                   (userid, quizid, sent, answer, result))
    #
    conn.commit()
    conn.close()


def get_quiz(id, user):
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    if user in ['admin', 'fabioja']:
        cursor.execute(
            "SELECT id, release, expire, problem, tests, results, diagnosis, numb from QUIZ where id = {0}".format(id))
    else:
        cursor.execute(
            "SELECT id, release, expire, problem, tests, results, diagnosis, numb from QUIZ where id = {0} and release < '{1}'".format(
                id, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    info = [reg for reg in cursor.fetchall()]
    conn.close()
    return info


def set_info(pwd, user):
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE USER set pass = ? where user = ?", (pwd, user))
    conn.commit()
    conn.close()


def get_info(user):
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute(f"SELECT pass, type from USER where user = '{user}'")
    print(f"SELECT pass, type from USER where user = '{user}'")
    info = [reg[0] for reg in cursor.fetchall()]
    conn.close()
    if not info:
        return None
    return info[0]


auth = HTTPBasicAuth()

app = Flask(__name__, static_url_path='')
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?TX'


@app.route('/', methods=['GET', 'POST'])
@auth.login_required
def main():
    """

    :return:
    """
    msg = ''
    status = 1
    challenges = get_quizes(auth.username())
    sent = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if request.method == 'POST' and 'ID' in request.args:
        id = request.args.get('ID')
        quiz = get_quiz(id, auth.username())
        if not quiz:
            msg = "Boa tentativa, mas não vai dar certo!"
            status = 2
            return render_template('index.html', username=auth.username(), challenges=challenges, p=status, msg=msg)

        quiz = quiz[0]
        if sent > quiz[2]:
            msg = "Sorry... Prazo expirado!"

        files = request.files['code']
        filename = './upload/{0}-{1}.py'.format(auth.username(), sent)
        files.save(filename)
        with open(filename, 'r') as file:
            answer = file.read()

        # lamb = boto3.client('lambda')
        args = {"ndes": id, "code": answer, "args": eval(quiz[4]), "resp": eval(quiz[5]), "diag": eval(quiz[6])}

        # response = lamb.invoke(FunctionName="Teste", InvocationType='RequestResponse', Payload=json.dumps(args))
        # feedback = response['Payload'].read()
        # feedback = json.loads(feedback).replace('"','')
        feedback = lambda_handler(args, '')

        result = 'Erro'
        if not feedback:
            feedback = 'Sem erros.'
            result = 'OK!'

        set_user_quiz(auth.username(), id, sent, feedback, result)

    if request.method == 'GET':
        if 'ID' in request.args:
            id = request.args.get('ID')
        else:
            id = 1

    if not challenges:
        msg = "Ainda não há desafios! Volte mais tarde."
        status = 2
        return render_template('index.html', username=auth.username(), challenges=challenges, p=status, msg=msg)
    quiz = get_quiz(id, auth.username())

    if not quiz:
        msg = "Oops... Desafio invalido!"
        status = 2
        return render_template('index.html', username=auth.username(), challenges=challenges, p=status, msg=msg)

    answers = get_user_quiz(auth.username(), id)

    return render_template('index.html', username=auth.username(), challenges=challenges, quiz=quiz[0],
                           e=(sent > quiz[0][2]), answers=answers, p=status, msg=msg, expi=convert_date(quiz[0][2]))


@app.route('/pass', methods=['GET', 'POST'])
@auth.login_required
def change():
    """

    :return:
    """
    if request.method == 'POST':
        velha = request.form['old']
        nova = request.form['new']
        repet = request.form['again']

        status = 1
        msg = ''
        if nova != repet:
            msg = 'As novas senhas nao batem'
            status = 3
        elif get_info(auth.username()) != hashlib.md5(velha.encode()).hexdigest():
            msg = 'A senha antiga nao confere'
            status = 3
        else:
            set_info(hashlib.md5(nova.encode()).hexdigest(), auth.username())
            msg = 'Senha alterada com sucesso'
            status = 3
    else:
        msg = ''
        status = 3

    return render_template('index.html', username=auth.username(), challenges=get_quizes(auth.username()), p=status, msg=msg)


@app.route('/logout')
def logout():
    """

    :return:
    """
    return render_template('index.html', p=2, msg="Logout com sucesso"), 401


@auth.get_password
def get_password(username):
    """

    :param username:
    :return:
    """
    return get_info(username)


@auth.hash_password
def hash_pw(password):
    """

    :param password:
    :return:
    """
    return hashlib.md5(password.encode()).hexdigest()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
