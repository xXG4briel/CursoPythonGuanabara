###Desafio 045


'''Crie um programa que faça o computador jogar jokenpô
com voce'''
from time import  sleep
from random import choice
lose='Voce perdeu'
win='Voce ganhou'

while 0==0:
    print('\n\n{:=^40}\n\n'.format('JOKENPô'))
    EU=str(input('Escolha PEDRA, PAPEL, OU TESOURA: ')).upper()
    PPT=str('PEDRA PAPEL TESOURA').split()
    GAME=choice(PPT)
    print('A Máquina escolheu {}'.format(GAME))
    if EU==GAME:
        print('Empate')
    elif EU=='TESOURA' and GAME=='PAPEL':
        print(win)
    elif EU=='TESOURA' and GAME=='PEDRA':
        print(lose)
    elif EU=='PAPEL' and GAME=='TESOURA':
        print(lose)
    elif EU=='PAPEL' and GAME=='PEDRA':
        print(win)
    elif EU=='PEDRA' and GAME=='PAPEL':
        print(lose)
    elif EU=='PEDRA' and GAME=='TESOURA':
        print(win)
    else:
        print(lose)
