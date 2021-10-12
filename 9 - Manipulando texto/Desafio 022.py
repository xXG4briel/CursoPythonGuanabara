##Desafio 022

"""Crie um programa que leia o nome
completo de uma pessoa e mostre :

    O nome com todas as letras maiúsculas

    O nome com todas as letras minusculas

    Quantas letras ao todo sem considerar espaços

    Quantas letras tem o primeiro nome"""

nom=input('digite  seu nome: ')
ftnome=nom.split()
space=int(nom.count(' '))
anali=len(nom)
print('Em maiusculo fica {}\n'.format(nom.upper()))
print('Em minusculo fica {}\n'.format(nom.lower()))
    #print(anali-space)
print('Sem contar os espaços tem um total de {} letras'.format(anali-space))
print('o primeiro nome tem um total de {} letras'.format(len(ftnome[0])))
