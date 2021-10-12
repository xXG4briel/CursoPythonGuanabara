#59 crie um programa que leia dois valores e mostre um menu na tela: 

from random import randint

x=y=0
menu=0
randx=0
randy=0

while menu!=5:
    menu=int(input('\n\n[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5]sair do programa\nDigite: '))
    if menu<5:
        x=int(input('Digite um valor: '))
        y=int(input('Digite mais um valor: '))
        if menu==1:
            print(f'\nA soma é {x+y}')
        if menu==2:
            print(f'\nA multiplicação é {x*y}')
        if menu==3:
            print((f'\n{x} é maior que {y}') if x>y else(f'\n{y} é maior que {x}'))
        if menu==4:
            randx=randint(0,100)
            randy=randint(0,100)
            print(f'\nO primeiro número digitado foi {x} e seu novo número é {randx}\n')
            print(f'O segundo número foi {y} e seu novo número é {randy}\n')
