from django.shortcuts import render
from .models import Materia
# Create your views here.

def inicio_vista(request):
    # Obtener todos los registros de la tabla "Materia"
    Listadomaterias=Materia.objects.all()
    return render(request, 'Gestionar materia.html', {'Lasmaterias':Listadomaterias})
