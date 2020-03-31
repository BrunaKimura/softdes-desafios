import sqlite3


def add_quiz(user, pwd, type):
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute('Insert into QUIZ(numb, release, expire, problem, tests, results, diagnosis) values ("{1}","{2}","{3}","{4}","{5}","{6}","{7}");'.format(numb, release, expire, problem, tests, results, diagnosis))
    conn.commit()
    conn.close()


with open('quiz.csv', 'r') as file:
    lines = file.read().splitlines()

for quiz in lines:
    (numb, release, expire, problem, tests, results, diagnosis) = quiz.split(',')
    add_quiz(numb, release, expire, problem, tests, results, diagnosis)