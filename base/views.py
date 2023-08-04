from django.shortcuts import render
from django.http import HttpResponse

#Definindo a View - Função 
def inicio(request):
    return render(request, 'inicio.html')

def contato(request):
    contexto = {
        'telefone': '(99) 99999-9999',
        'responsavel': 'Igor phellipe da silva passos'
    }
    if request.method == 'POST':
        #Submissão de dados enviados pelo formulário, e mostrar como print o que foi enviado
        print(request.POST)
        print(request.POST['Nome'])
        print(request.POST['E-mail'])
        print(request.POST['Mensagem'])
    return render(request, 'contato.html', contexto)