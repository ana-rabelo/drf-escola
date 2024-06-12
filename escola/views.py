from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, AlunoSerializerV2, CursoSerializer, ListaAlunosCursoSerializer, ListaMatriculasAlunoSerializer, MatriculaSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibe todos os alunos"""

    queryset = Aluno.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return AlunoSerializerV2
        return AlunoSerializer

class CursosViewSet(viewsets.ModelViewSet):
    """Exibe todos os cursos"""

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class MatriculasViewSet(viewsets.ModelViewSet):
    """Lista todas as matrículas"""

    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListaMatriculasAluno(generics.ListAPIView):
    """Lista as matrículas de um aluno"""

    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ListaMatriculasAlunoSerializer

class ListaAlunosCurso(generics.ListAPIView):
    """Lista os alunos matriculados em um curso"""

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset                    
    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ListaAlunosCursoSerializer