'''Desafio 039

Faça um programa que leia o ano de nascimento de um jovem e informe,de acordo com sua idade:

    SE ELE ainda vai se alistar ao serviço militar
    Se é a hora de se alistar.
    Se já passou do tempo do alistamento

OBS: SEU PROGRAMA TAMBÉM DEVERÁ MOSTRAR O TEMPO QUE FALTA OU QUE PASSOU DO PRAZO'''

from datetime import date
x=int(input('Qual seu ano de Nascimento? '))
idade=date.today().year-x

if idade<18:
    print('Você ainda tem tempo para curtir recruta!\n')
elif idade==18:
    print('Chegou a hora de se alistar!\n')
elif idade>18:
    print('Você passou do tempo de se alistar ')
