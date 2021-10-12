'''DESAFIO 036

Escreva um programa para aprovar o empréstimo bancário
para a compra
de uma casa.O programa vai perguntar o VALOR DA CASA, o SALÁRIO do comprador
e em QUANTOS ANOS ELE VAI PAGAR
calcule o valor da prestação mensal sabendo ela não pode exceder 30% do salário
ou então o empréstimo será negado'''


x=float(input('\033[0:35:42mValor da casa: R$'))
y=float(input('Salário do comprador: R$'))
z=float(input('Quantos anos de financiamento? '))
mensal=x/(z*12)
print('O valor da casa R${:.2f} pago em {} anos\nDaria um total de R${:.2f}'.format(x,z,mensal))
if mensal>=y*0.3:
    print('\nEmpréstimo NEGADO')
else:
    print('\nEmprèstimo aprovado')
