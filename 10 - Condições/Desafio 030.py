"""DESAFIO 030

CRIE UM PROGRAMA COM UM NUMERO INTEIRO E MOSTRE SE LE É PAR OU ÍMPAR"""

print('{:=^80}{:^80}{:=^80}'.format('=','Par ou ímpar?','='))
a=int(input('Digite um valor '))

if (a%2)==0:
    print('PAR')
else:
    print('ÍMPAR')

