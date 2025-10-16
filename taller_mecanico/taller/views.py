from django.shortcuts import render
from .models import Cliente, Persona

def lista_clientes(request):
    clientes = Cliente.objects.select_related('dni').all()
    return render(request, 'taller/lista_clientes.html', {'clientes': clientes})
