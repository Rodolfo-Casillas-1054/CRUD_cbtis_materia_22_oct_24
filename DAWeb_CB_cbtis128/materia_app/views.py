from django.shortcuts import render

# Create your views here.

def inicio_vista(request):
    return render(request, 'Gestionar materia.html')
