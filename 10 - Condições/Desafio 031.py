"""DESAFIO 031

Desenvolva um programa que pergunte a distãncia de uma viagem em km calcule o preço da passagem, cobrando
R$0,50 por KM para viagens de até 200KM e R$0,45 PARA VIAGENS MAIS LONGAS."""

print('{:=^80}{:^80}{:=^80}'.format('=','Calculo sua Viagem','='))
print('\n\nOlá vou te ajudar a calcular a viagem!')
a=float(input('Quantos km são?'))
if a<=200:
    print('Deu um total de R${}'.format(a*0.5))
elif a>=201:
    print('\n. . .Uau Viagem Longa!\nDeu um total de R${}'.format(a*0.45))
else:
    print('ok')
