# Desafios de Software
Este projeto é uma atividade da matéria [Desenvolvimento Aberto](https://insper.github.io/dev-aberto/),
em que a proposta era reformar um código mal feito e criar uma página web para ele (Projeto Profissional).
A página pode ser encontrada no link a seguir: https://brunakimura.github.io/softdes-desafios/.

### Instruções:
#### Para modificar as páginas do Mkdocs em tempo real:
```
PYTHONPATH=src mkdocs serve
```

#### Para buildar as páginas do Mkdocs no Github pages:
```
PYTHONPATH=src mkdocs gh-deploy -c
```

#### Testes de interface:
Para fazer os testes de interface, você precisa ter o driver do Selenium para seu navegador no PATH.

#### Testes Pytest:
Para executar os testes da lambda_function, execute o commando `pytest` na pasta `tests`.