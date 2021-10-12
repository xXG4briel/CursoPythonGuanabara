'''Desafio 043

Densevolva uma lógica que leia o peso e a altura de um a pessoa, calcule
seu imc e mostre seu status , de acordo com a tabela abaixo:

    18.5Abaixo do peso
    18.5 e 25 Peso ideal
    25 até 30: Sobrepeso
    30 a 40: Obesidade
    acima de 40:Obesidade Mórbida'''

from math import ceil
IMC=str('ABAIXO_DO_PESO PESO_IDEAL SOBREPESO OBESIDADE OBESIDADE_MÓRBIDA').split()
print('{:=^40}\n{:^45}\n'.format('ÍNDICE DE MASSA CORPORAL','IMC'))
x=float(input('Digite sua altura'))
x=float(input('Digite seu peso:'))/(x*x)
if x<18.5:
    print(IMC[0])
elif x>=18.5 and x<=25:
    print(IMC[1])
elif x>=25and x<=30:
    print(IMC[2])
elif x>=30 and x<=40:
    print(IMC[3])
else:
    print(IMC[4])
