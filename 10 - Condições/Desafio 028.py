"""DESAFIO 28

ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR 'PENSAR' EM UM NÚMERO INTEIRO
ENTRE 0 E 5 E PEÇA
PARA O USUARIO TENTAR DESCOBRIR QUAL FOI O NÚMERO ESCOLHIDO PEL COMPUTADOR.

O PROGRAMA DEVERÁ ESCREVER NA TELA SE O USUÁRIO VENCEU OU PERDEU"""


import random
a=random.randint(0,5)
print('===============================================================================\n{:^80}\n==============================================================================='.format('JOGO DO ADIVINHÃO'))
b=int(input('\n\nVamos brincar ?\n\nDigite um valor entre 0 e 5 e vou dizer se voce acertou!'))
if b==a:
    print('Voce acertou meu numero era {} !\nParabéns'.format(a))
else:
    print('Errado X\nMeu número era {}'.format(a))

