from django.shortcuts import render

def inicio(request):
    return render(request, 'taller/inicio.html')

def acerca(request):
    return render(request, 'taller/acerca.html')

def servicios(request):
    return render(request, 'taller/servicios.html')

def contacto(request):
    return render(request, 'taller/contacto.html')

def cotizacion(request):
    return render(request, 'taller/cotizacion.html')

def login_empleados(request):
    return render(request, 'taller/login.html')
