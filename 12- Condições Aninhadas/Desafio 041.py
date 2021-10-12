'''Desafio 041

A confereção Nacional de natação precisa de um program
que leia o ano de nascimento de  um atleta e mostre sua categoria
de acordo com a idade:
    9:MIRIM
    14:INFATIL
    19:JUNIOR
    20:SÊNIOR
    ACIMA:MASTER'''

print('CLUBE DE NATAÇÃO')
x=float(input('Qual sua idade'))
if x>=9 and x<=14:
    print('Mirim')
elif x>=14 and x<=19:
    print('Infatil')
elif x==19:
    print('Junior')
elif x==20:
    print('Sênior')
elif x>20:
    print('Master')
