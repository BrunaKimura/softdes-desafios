# Professores

## Introdução

## Configurando o Ambiente
O primeiro passo para utilizar o servidor é configurar o ambiente. Antes de tudo é necessário criar o banco de dados(BD) onde será armazenado tanto as perguntas dos desafios como os usuários da ferramenta, ou seja, os alunos.

Para tanto é necessário instalar o gerenciador do BD, sqlite3. Execute o comando abaixo em um novo terminal (Crtl+Shift+T) para instalar o sqlite3.

```$ pip install pysqlite3```

Com o gerenciador instalado o próximo passo é criar o banco de dados utilizando o sqlite3. O comando abaixo permite criar um BD com o nome "quiz", este comando deve ser executado na pasta `\src` do projeto. 

```$ sqlite3 quiz.db```

Ao Executar o comando um documento chamado `quiz.db` será criado na mesma pasta e o seu terminal deverá estardentro do ambiente do sqlite3.
Para checar se o banco de dados foi devidamente criado, execute o seguinte comando no sqlite3.

``` sqlite> .database```

A função deve retornar o caminho até o documento `quiz.db`. Com isso feito, agora é necessário criar as tabelas do projeto. Assim, deve-se executar o seguinte comando:

``` sqlite> .read quiz.sql```


Ou simplesmente execute o comando abaixo, assim irá criar o banco de dados e redirecionar as tabelas para o mesmo.

```$ sqlite3 quiz.db < quiz.sql```

Para checar se as tabelas foram de fato criadas execute o seguinte comando:

```sqlite> .tables ```

O retorno será as tabelas do projeto. Neste caso:
```QUIZ      USER      USERQUIZ```

## Adicionando os Usuários (Alunos)

O primeiro passo é criar um documento `.csv`, na pasta `\src` do projeto. O comando abaixo irá criar o documento e abrir para a edição no editor *nano*.

```$ nano users.csv```

Adicione os alunos e sua senha separando com vírgulas: aluno, senha

![Adiciona aluno](img/add_alunos.png)

Para salvar o arquivo basta utilizar o comando Gravar (Ctrl+O) e então fechar o arquivo (Ctrl+X). 

Com o arquivo editado o próximo passo é adicionar esses novos valores a tabela, ou seja, popular a tabela `USER`. Para isso basta executar o arquivo python `adduser.py`.

```$ python adduser.py```

Não é necessário passar o arquivo como argumento, apenas é estritamente necessário criar o arquivo com o nome `users.csv`. Agora o projeto já possui os seus usuários!

## Adicionando Novos Desafios