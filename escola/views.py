from rest_framework import viewsets, generics, status
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, AlunoSerializerV2, CursoSerializer, ListaAlunosCursoSerializer, ListaMatriculasAlunoSerializer, MatriculaSerializer
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibe todos os alunos"""

    queryset = Aluno.objects.all()

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return AlunoSerializerV2
        return AlunoSerializer

class CursosViewSet(viewsets.ModelViewSet):
    """Exibe todos os cursos"""

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    http_method_names = ['get', 'post', 'put', 'pach']

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            id = str(serializer.data['id'])
            response['Location'] = self.request.build_absolute_uri() + id
            return response

class MatriculasViewSet(viewsets.ModelViewSet):
    """Lista todas as matrículas"""

    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    http_method_names = ['get', 'post', 'put', 'patch']

    @method_decorator(cache_page(30))   
    def dispatch(self, *args, **kwargs):
        return super(MatriculasViewSet, self).dispatch(*args, **kwargs)

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