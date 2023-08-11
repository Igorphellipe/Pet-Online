from django.shortcuts import render
from django.http import HttpResponse
from base.forms  import ContatoForm, ReservaPet
from base.models import Contato, Reserva
#Definindo a View - Função 
def inicio(request):
    return render(request, 'inicio.html')

def contato(request):
    sucesso = False
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        sucesso = True
        form.save()
    contexto = {
        'telefone': '(99) 99999-9999',
        'responsavel': 'Igor Phellipe',
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'contato.html', contexto)

def reserva(request):
    sucesso = False
    form = ReservaPet(request.POST or None)
    if form.is_valid():
        sucesso = True
        nome_do_pet = form.cleaned_data['Nome_do_Pet']
        telefone = form.cleaned_data['Telefone']
        dia_da_reserva = form.cleaned_data['Dia_Reserva']
        observacao = form.cleaned_data['Observacao']
        Reserva.objects.create(nome_do_pet=nome_do_pet, telefone=telefone, dia_da_reserva=dia_da_reserva, observacao=observacao)
    contexto = {
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'reserva.html', contexto)