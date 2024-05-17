"""
    Vista para la página de inicio.
"""
from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, 'paginas/index.html')
def mision(request):
    return render(request, 'paginas/mision.html')
def vision(request):
    return render(request, 'paginas/vision.html')
def valores(request):
    return render(request, 'paginas/valores.html')