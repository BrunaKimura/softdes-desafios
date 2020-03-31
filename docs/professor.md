# Professores

## Adicionando os Usuários (Alunos)

O primeiro passo é criar um documento `.csv`, na pasta `src/` do projeto. O comando abaixo irá criar o documento e abrir para a edição no editor *nano*.

```$ nano users.csv```

Para adicionar os usuários é necessário escrever o login e o seu tipo sepados por vírgulas, sendo que este último pode ser `admin` para administrador ou `aluno` para os alunos. Cada linha recebe a informação de um usuário. Adicione primeiramenta na primeira linha o administrador da página (admin, admin) e em seguida os alunos.

![Adiciona aluno](img/add_alunos.png)

Para salvar o arquivo basta utilizar o comando Gravar (Ctrl+O) e então fechar o arquivo (Ctrl+X). A senha poderá ser alterada posteriormente pelo aluno.

Com o arquivo editado o próximo passo é adicionar esses novos valores a tabela, ou seja, popular a tabela `USER`. Para isso basta executar o arquivo python `add_user.py`.

```$ python add_user.py```

Não é necessário passar o arquivo como argumento, apenas é estritamente necessário criar o arquivo com o nome `users.csv`. Agora o projeto já possui os seus usuários!

## Adicionando Novos Desafios

Adicionar novos desafios é muito parecido com a forma como os usuários são adicionados. Da mesma forma que no caso anterior, é necessário criar um arquivo `.csv`, na pasta `src/` do projeto, mas agora, o nome do arquivo será `quiz.csv`.

```$ nano quiz.csv```

A cada linha será inserido as informações de cada desafio. A estrutura para adiconar um novo desafio é (numb, release, expire, problem, tests, results, diagnosis), sendo os seus significados:

- **numb**: Numeração do desafio
- **release**: Data de lançamento
- **expire**: Data de validade
- **problem**: Descrição do desafio
- **test**: Possíveis entradas da função
- **result**: Resultados das entradas fornecidas pelo **test**
- **diagnosis**: ?

![Adiciona quiz](img/add_quiz.png)

O seu arquivo deve ficar semelhante com a imagem acima.

Para enviar os teste para o servidor basta executar o arquivo python `add_quiz.py`.

```$ python add_quiz.py```

Agora o projeto já possui os desafios!