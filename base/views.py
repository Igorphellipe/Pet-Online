from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from base.forms  import ContatoForm, ReservaPet
from base.models import Contato, Reserva

#Definindo a View Inicio- Função 
def inicio(request):
    return render(request, 'inicio.html')
#View de Contato
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
#View de Reserva
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
#View de Usuário login
def login_usuario(request):
    if request.method == 'GET':
        formulario = AuthenticationForm()
        return render(request, 'login.html', {'formulario': formulario})
    
    else:
        nome_usuario = request.POST['username']
        senha = request.POST ['password']
        usuario = authenticate(request, username=nome_usuario, password=senha)
        if usuario is not None:
            login(request, usuario)
            return redirect('inicio')
        else:
            formulario = AuthenticationForm()
            return render(request, 'login.html', {'formulario': formulario, 'erro': 'Usuário ou senha invalidos'})
        

#View de logout 
def logout_usuario(request):
    logout(request)
    return redirect('inicio')

def novo_usuario(request):
    if request.method == 'GET':
        formulario = UserCreationForm()
        return render (request, 'novo_usuario.html', {'formulario': formulario})
    
    else:
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')

def apis_disp(request):
    return render (request, 'api_disp.html')