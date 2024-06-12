# <img src=https://i.imgur.com/5ustGMp.png width="250"> </img>

A **API DRF Escola** é um app de escola, onde temos alunos, cursos e alunos matriculados em diferentes cursos. A API é capaz de:

- Criar e atualizar um aluno;
- Criar, atualizar e remover um curso;
- Criar uma matrícula de um aluno;

### Ferramentas
A API foi construída com Django REST framework, que ajuda nos processos intermediários entre os dados que estamos criando e o cadastro das URLs e das rotas principais da nossa aplicação.

## Baixando o projeto
Primeiramente, precisamos ter o projeto em nossa máquina. Isso pode ser feito de duas maneiras:

1. Executando o comando git clone https://github.com/ana-rabelo/django-rest-api no terminal, no diretório onde você deseja salvar o projeto. Isso criará uma pasta chamada django-rest-api com os arquivos do projeto. Ou
2. Baixando o projeto como um arquivo zip através do link https://github.com/ana-rabelo/django-rest-api/archive/refs/heads/main.zip e extraindo-o.

## Preparando o ambiente
Para executar o projeto, certifique-se de ter o Python instalado na sua máquina. Se você não o tiver, pode baixá-lo do site oficial https://www.python.org/downloads/.

Também precisamos ter o pip instalado. Execute o comando python get-pip.py no terminal para instalá-lo.

Após instalar o Python e o pip, abra o terminal e navegue até a pasta do projeto. Em seguida, execute os seguintes comandos:

- `pip install virtualenv` para instalar o pacote de ambiente virtual.
- `python -m virtualenv .venv` para criar um ambiente virtual.
- `source .venv/bin/activate` para ativar o ambiente virtual no Linux ou `.venv/Scripts/activate` no Windows.
- `pipenv check` para verificar se o ambiente atual está a cumprir os requisitos do Pipfile.

Agora, precisamos criar o banco de dados. Execute os seguintes comandos:

- `python manage.py makemigrations` para criar os arquivos de migração.
- `python manage.py migrate` para aplicar as migrações e criar o banco de dados.
 
Finalmente, podemos executar o projeto:

- `python manage.py runserver` para iniciar o servidor.

Para popular o banco de dados e criar usuários com permissões específicas para este projeto, execute o comando em um novo terminal na raiz do projeto:

- `python seed.py`

O script `seed.py` cria usuários no Django com permissões específicas. Ele também popula o banco de dados com dados de exemplo, se necessário. Verifique e personalize o script de acordo com suas necessidades.
  
Após executar o último comando, o terminal exibirá uma mensagem com o endereço onde a API está sendo executada. Pressione **Ctrl + Clique** no link para abrir no seu navegador.

