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
        email = '{}@{}'.format(nome.lower(),fake.free_email_domain())
        email = email.replace(' ', '')
        rg = "{}{}{}{}".format(random.randrange(10, 99),random.randrange(100, 999),random.randrange(100, 999),random.randrange(0, 9)) 
        cpf = cpf.generate()
        data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=30)
        celular = "{} 9{}-{}".format(random.randrange(10, 89), random.randrange(4000, 9999), random.randrange(4000, 9999))
        
        a = Aluno(nome=nome,rg=rg, cpf=cpf,data_nascimento=data_nascimento, celular=celular, email=email)
        a.save()

def criando_cursos(quantidade_de_cursos):
    """Cria cursos com código, descrição e nível aleatórios."""

    dados = [
        ('CPOO1', 'Curso de Python Orientação à Objetos 01'),
        ('CPOO2', 'Curso de Python Orientação à Objetos 02'),
        ('CPOO3', 'Curso de Python Orientação à Objetos 03'),
        ('CDJ01', 'Curso de Django 01'),
        ('CDJ02', 'Curso de Django 02'),
        ('CDJ03', 'Curso de Django 03'),
        ('CDJ04', 'Curso de Django 04'),
        ('CDJ05', 'Curso de Django 05'),
        ('CDJRF01', 'Curso de Django REST Framework 01'),
        ('CDJRF02', 'Curso de Django REST Framework 02'),
        ('CDJRF03', 'Curso de Django REST Framework 03'),
        ('CDJRF04', 'Curso de Django REST Framework 04')
    ]
    
    for _ in range(quantidade_de_cursos):
        for codigo, descricao in dados:
            nivel = random.choice("BIA")
            Curso.objects.create(codigo=codigo, descricao=descricao, nivel=nivel)

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

criando_alunos(50)
criando_cursos(5)

criando_usuarios('Maria', 'maria@example.com', 'senha_segura', 'Silva', [Matricula], ['add', 'view', 'change'])
criando_usuarios('Marcos', 'marcos@example.com', 'senha_segura', 'Pereira', [Aluno, Curso], ['add', 'view', 'change'])