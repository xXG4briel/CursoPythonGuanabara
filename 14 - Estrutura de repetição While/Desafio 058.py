'''Melhore o jogo do desafio 28 onde o computador vai pensar em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
palpites foram necessários para vencer.'''

from random import randint
randomizar = 10

jogador = 0
chance = 0

while randomizar != jogador:
    randomizar = randint(0,10)
    jogador = int(input('Digite um números de  0 a 10: '))
    if jogador != randomizar:
        print(f'Voce errou !\n')
        chance+=1
print(f'\n\nVoce acertou !!!\nMeu número foi  {jogador}\nVoce acertou depois de {chance} chances')
    

