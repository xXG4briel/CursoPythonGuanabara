##Desafio 023

"""faça um programa que leia um número de 0 a9999 e mostre
na tela cada um dos dígitos separados

ex:digite um número: 1834

unidade:4
dezena:3
centeba:8
milhar:1
"""

n1=input('digite um valor até 9999: ')

print('unidade {}\n dezena {}\n centena {}\n milhar {}'.format(n1[3],n1[2],n1[1],n1[0]))
