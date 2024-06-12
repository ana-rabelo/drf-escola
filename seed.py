import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF
import random
from escola.models import  Aluno, Curso, Matricula
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType 

def criando_alunos(quantidade_de_pessoas):
    """Cria pessoas com nome, cpf, rg e data de nascimento aleatórios."""

    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_pessoas):
        cpf = CPF()
        nome = fake.name()
        rg = "{}{}{}{}".format(random.randrange(10, 99),random.randrange(100, 999),random.randrange(100, 999),random.randrange(0, 9)) 
        cpf = cpf.generate()
        data_nascimento = fake.date_between(start_date='-18y', end_date='today')
        a = Aluno(nome=nome,rg=rg, cpf=cpf,data_nascimento=data_nascimento)
        a.save()

def criando_cursos(quantidade_de_cursos):
    """Cria cursos com código, descrição e nível aleatórios."""

    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_cursos):
        codigo_curso = "{}{}-{}".format(random.choice("ABCDEF"), random.randrange(10, 99),random.randrange(1, 9))
        descs = ['Python Fundamentos', 'Python intermediário','Python Avançado', 'Python para Data Science', 'Python/React']
        descricao = random.choice(descs)
        descs.remove(descricao)
        nivel = random.choice("BIA")
        c = Curso(codigo_curso=codigo_curso,descricao=descricao, nivel=nivel)
        c.save()

def criando_usuarios(username, email, password, last_name, models, permissions):
    """Cria um usuário com permissões específicas."""

    if not User.objects.filter(username=username).exists():
        novo_usuario = User.objects.create_user(username, email, password)

        novo_usuario.first_name = username
        novo_usuario.last_name = last_name
        novo_usuario.is_active = True

        for model in models:
            content_type = ContentType.objects.get_for_model(model)
            for permissao in permissions:
                permissao = Permission.objects.get(content_type=content_type, codename=f'{permissao}_{model.__name__.lower()}')
                novo_usuario.user_permissions.add(permissao) 

        novo_usuario.save()
    else:
        print("Usuário já existe.")

criando_alunos(200)
criando_cursos(5)

criando_usuarios('Maria', 'maria@example.com', 'senha_segura', 'Silva', [Matricula], ['add', 'view', 'change'])
criando_usuarios('Marcos', 'marcos@example.com', 'senha_segura', 'Pereira', [Aluno, Curso], ['add', 'view', 'change'])