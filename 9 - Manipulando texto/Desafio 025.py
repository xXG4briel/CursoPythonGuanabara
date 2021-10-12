##Desafio 025

"""Crie um programa que leia o nome de uma pessoa e diga dse ela tem
'SILVA' no nome"""

sil=str(input('Digite seu nome completo\n   ')).lower()
print('Tem silva no nome: {}'.format('silva' in sil))
