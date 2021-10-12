'''Desafio 038

Escreva um programa que leia dois números

inteiros e compare-os, mostrando na tela
uma mensagem:

    -o primeiro valor é maior
    -o segudno valor é maior
    -não exite valor   maior, os dois são iguais'''
x=float(input('Digite um numero: '))
y=float(input('Digite outro numero: '))

if x>y:
    print('O primeiro valor é maior')
elif  y>x:
    print('O Segundo valor é maior')
elif x==y:
    print('Ambos são iguais')
