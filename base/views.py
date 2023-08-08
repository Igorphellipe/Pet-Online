from django.shortcuts import render
from django.http import HttpResponse
from base.forms  import ContatoForm
#Definindo a View - Função 
def inicio(request):
    return render(request, 'inicio.html')

def contato(request):
    sucesso = False
    if request.method == 'GET':
        form = ContatoForm()
    else:
        form = ContatoForm(request.POST)
        if form.is_valid():
            sucesso = True
    contexto = {
        'telefone': '(99) 99999-9999',
        'responsavel': 'Igor Phellipe',
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'contato.html', contexto)