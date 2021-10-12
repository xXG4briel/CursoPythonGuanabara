##Desafio 026

""" Faça um programa que leia uma frase pelo teclado e mostre :

    Quantas vezes aparece a letra "A"

    em que posição ela aparece a primeira vez

    Em que posição ela aparece a última vez"""

s=str(input('digite seu nome: '))
smin=s.lower()
print('a letra a minusculo aparece um total de : {}'.format(s.count('a')))
print('a letra a maiusculo aparece um total de : {}'.format(s.count('A')))
print('Ela aparece a primeira vez em {}'.format(s.find('a')+1))
print('Em que posição ela aparece a última vez {}'.format(s.find('a',-1)+1))
