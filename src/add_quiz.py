import sqlite3


def add_quiz(numb, release, expire, problem, tests, results, diagnosis):
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute(
        "Insert into QUIZ(numb, release, expire, problem, tests, results, diagnosis) values ({0}, '{1}','{2}','{3}','{4}','{5}','{6}')".format(numb, release, expire, problem, tests, results, diagnosis))
    conn.commit()
    conn.close()

# quizes = pd.read_csv("quiz.csv")
# print(quizes)
# #
# # with open('quiz.csv', 'r') as file:
# #     lines = file.read().splitlines()
# #
# # for quiz in lines:
# #     print(eval(quiz))
# #     numb, release, expire, problem, tests, results, diagnosis = quiz
# #     add_quiz(numb, release, expire, problem, tests, results, diagnosis)

add_quiz(2, '2020-05-04', '2020-12-31 23:59:59', 'Exemplo de problema da bruna hehe', '[[1],[2],[3]]', '[1, 2, 3]', '["nao deu 1","nao deu 2","nao deu 3"]')
