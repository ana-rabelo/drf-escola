from rest_framework import serializers
from escola.models import Aluno, Curso

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        # fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']
        # Podemos usar '__all__' para pegar todos os campos do model ou "filtrar" os campos que queremos disponibilizar na API 
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'