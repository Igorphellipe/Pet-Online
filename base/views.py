from django.shortcuts import render
from django.http import HttpResponse

#Definindo a View - Função 
def inicio(request):
    return render(request, 'inicio.html')

def contato(request):
    return render(request, 'contato.html')