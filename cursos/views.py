# cursos/views.py
from django.shortcuts import render
from .models import Curso

def lista_cursos(request):
    cursos = Curso.objects.all()  # Obtiene todos los cursos
    return render(request, 'cursos/cursos.html', {'cursos': cursos})
