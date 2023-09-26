from django.shortcuts import render
import datetime as dt
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Contato, Reserva
from rest_framework.viewsets import ModelViewSet
from rest_api.serializers import AgendamentoModelSerializer, ContatoModelSerializer



class AgendamentoModelViewSet(ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = AgendamentoModelSerializer

class ContatoModelViewSet(ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoModelSerializer


@api_view(['GET', 'POST'])
def reservas(request):
    if request.method == 'POST':
        dados = request.data 
        nome_do_pet = dados['nome_do_pet']
        telefone = dados['telefone']
        dia_da_reserva = dt.datetime.strptime(dados['dia_da_reserva'], '%d/%m/%y').date()
        observacao = dados['observacao']
        reserva = Reserva.objects.create(nome_do_pet=nome_do_pet, telefone=telefone, dia_da_reserva=dia_da_reserva, observacao=observacao
        )
        dados_reserva = {
            'id': reserva.id,
            'nome_do_pet': reserva.nome_do_pet,
            'telefone': reserva.telefone,
            'dia_da_reserva': reserva.dia_da_reserva,
            'observacao': reserva.observacao,
        }
        return Response(data=dados_reserva)
    else:
        reservas = Reserva.objects.all()
        dados = []
        for reserva in reservas:
            dados.append({
                'nome_do_pet': reserva.nome_do_pet,
                'telefone': reserva.telefone,
                'dia_da_reserva': reserva.dia_da_reserva,
                'observacao': reserva.observacao,
            })
        return Response(data=dados)

#Código feito com o professor.
@api_view(['GET', 'POST'])
def contatos(request):
    if request.method == 'POST':
        dados = request.data
        nome = dados['nome']
        email = dados['email']
        mensagem = dados['mensagem']
        contato = Contato.objects.create(nome=nome, email=email, mensagem=mensagem)
        dados_contato = {
            'id': contato.id,
            'nome': contato.nome,
            'email': contato.email,
            'mensagem': contato.mensagem
        }
        return Response(data=dados)
    else:
        contatos = Contato.objects.all()
        dados = []
        for contato in contatos:
            dados.append({
                'nome': contato.nome,
                'email': contato.email,
                'mensagem': contato.mensagem,
            })
        return Response(data=dados)


