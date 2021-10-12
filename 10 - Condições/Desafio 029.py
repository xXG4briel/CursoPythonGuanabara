"""DESAFIO 029

FAÇA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO

SE ELE ULTRAPASSAR 80KM/h, mostre uma mensagem dizendo que ele foi multado

a multa vai custar RS7,00 POR CADA KM ACIMA DO LIMITE"""

km=int(input('Quantos km voce andava nessa rodovia ? '))
if km<=80:
    print('Você não foi multado!')
else:
    a=int(input('Quantos Quilometros você andou nessa velocidade?'))
    print('Voce foi multado!\nNum valor de R${}'.format(7*a))
