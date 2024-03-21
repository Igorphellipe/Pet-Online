# Import do Basecommand 
from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from base.models import Petshop
from random import sample

#importando a Class Basecommand
class Command(BaseCommand):
    #Função criada para buscar os valores da PK de petshop e armazenar em uma lista 
    def list_petshops(self):
            return Petshop.objects.all().values_list('pk', flat=True)
    
    #Função criada para receber os paramentros do sorteio e mensagem de ajuda   
    def add_arguments(self, parser):
        parser.add_argument(
            'quantity',
            nargs ='?',
            default= 5,
            type= int,
            help= 'Quantas pessoas devem participar do concurso ?'
        )
        
        parser.add_argument(
            '-petshop',
            required= True,
            type= int,
            choices= self.list_petshops(),
            help= 'Petshop ID  para ser executado o consurso'
        )
    
    def escolher_reservas(self, banhos, quantidade):
        banhos_list = list(banhos)
        if quantidade > len (banhos_list):
            quantidade = len (banhos_list)
            
        return sample(banhos_list, quantidade)
    
    #Função para imprimir os dados do Petshop
    def imprimir_info_petshop(self, petshop):
        self.stdout.write(
            self.style.HTTP_INFO(
                'Dados do Petshop que realizou o sorteio'
            )
        )
        self.stdout.write(f'Nome do Petshop: {petshop.nome}')
        self.stdout.write(
            f'Endereço {petshop.rua}, {petshop.numero}, {petshop.bairro}'
        )
    
    # Função para imprimir dados dos Pets sorteados
    def imprimir_reservas_sorteadas(self, reservas):
        self.stdout.write(
            self.style.HTTP_INFO(
                'Dados dos Pets sorteados'
            )
        )
        self.stdout.write(
            self.style.HTTP_INFO(
                '=' * 35
            )
        )
        for reserva in reservas:
            self.stdout.write(
                f'Nome do Pet: {reserva.nome_do_pet}'
            )    
            self.stdout.write(
                f'Telefone Tutor: {reserva.telefone}'
            )
            self.stdout.write(
                self.style.HTTP_INFO(
                    '=' * 35
                )
            )
    
    # Função handle para buscar todos os banhos reservados comforme o ID do petshop
    def handle(self, *args, **options):
        quantity = options['quantity']
        petshop_id = options['petshop']
        
        petshop = Petshop.objects.get(pk=petshop_id)
        reservas = petshop.reservas.all()
        
        banhos_escolhidos = self.escolher_reservas(reservas, quantity)
    
        self.stdout.write(
            self.style.SUCCESS('Sorteio concluído')
        )
        
        self.imprimir_info_petshop(petshop)
        self.imprimir_reservas_sorteadas(banhos_escolhidos)