from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, ListaAlunosCursoSerializer, ListaMatriculasAlunoSerializer, MatriculaSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibe todos os alunos"""

    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursosViewSet(viewsets.ModelViewSet):
    """Exibe todos os cursos"""

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculasViewSet(viewsets.ModelViewSet):
    """Lista todas as matrículas"""

    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ListaMatriculasAluno(generics.ListAPIView):
    """Lista as matrículas de um aluno"""

    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaMatriculasAlunoSerializer

class ListaAlunosCurso(generics.ListAPIView):
    """Lista os alunos matriculados em um curso"""

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    
    serializer_class = ListaAlunosCursoSerializer