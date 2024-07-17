from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'recipes/home.html', {'name': 'Hosken'})

def sobre(request):
    return render(request, 'recipes/sobre.html')

def contato(request):
    return render(request, 'recipes/contato.html')