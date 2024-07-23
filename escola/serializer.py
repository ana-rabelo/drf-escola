from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula
from escola.validators import cpf_invalido, nome_invalido, celular_invalido


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento', 'foto']

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
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento', 'celular', 'foto']

class AlunoSerializerV3(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'cpf', 'data_nascimento', 'celular', 'email']

    def validate(self,dados):
        
        if cpf_invalido(dados['cpf']):
            raise serializers.ValidationError({'cpf':'O CPF deve ter um valor válido.'})
        if nome_invalido(dados['nome']):
            raise serializers.ValidationError({'nome':'O nome só pode ter letras'})
        if celular_invalido(dados['celular']):
            raise serializers.ValidationError({'celular':'O celular precisa seguir o padrão 99 99999-9999'})
        return dados