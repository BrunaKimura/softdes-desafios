import sys
sys.path.append('../src')

from servidor import lambda_handler

def test_success_lambda_function():
    event = { "ndes": 1,
              "code": open("./desafio_test1.py", "r").read(),
              "args": [[1], [2], [3]],
              "resp": [0, 0, 0],
              "diag": ['a', 'b', 'c']
            }
    response = lambda_handler(event, None)
    assert len(response) == 0


def test_error_lambda_function():
    event = { "ndes": 1,
              "code": open("./desafio_test2.py", "r").read(),
              "args": [[1], [2], [3]],
              "resp": [0, 0, 0],
              "diag": ['a', 'b', 'c']
            }
    response = lambda_handler(event, None)
    assert response == 'a b c'

def test_error2_lambda_function():
    event = { "ndes": 1,
              "code": open("./desafio_test3.py", "r").read(),
              "args": [[1], [2], [3]],
              "resp": [0, 0, 0],
              "diag": ['a', 'b', 'c']
            }
    response = lambda_handler(event, None)
    assert response == "Nome da função inválido. Usar 'def desafio1(...)'"