from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        #Podemos usar '__all__' para pegar todos os campos do model ou "filtrar" os campos que queremos disponibilizar na API 
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        #Também podemos usar o exclude para excluir campos que não queremos disponibilizar na API
        exclude = []

class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']
    
    def get_periodo(self, obj):
        """Retorna o nome do período ao invés do código do período."""
        return obj.get_periodo_display()
    
class ListaAlunosCursoSerializer(serializers.ModelSerializer):
    aluno = serializers.ReadOnlyField(source='aluno.nome')
    periodo = serializers.SerializerMethodField()
    
    class Meta:
        model = Matricula
        fields = ['aluno', 'periodo']
    
    def get_periodo(self, obj):
        """Retorna o nome do período ao invés do código do período"""
        return obj.get_periodo_display()
    
class AlunoSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento', 'celular']