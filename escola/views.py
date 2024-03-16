from django.http import JsonResponse

def alunos(request):
    if request.method == 'GET':
        alunos = [
            {'id': 1, 'nome': 'Eduardo'},
            {'id': 2, 'nome': 'Maria'},
            {'id': 3, 'nome': 'Ana'},
        ]
        return JsonResponse({'alunos': alunos})