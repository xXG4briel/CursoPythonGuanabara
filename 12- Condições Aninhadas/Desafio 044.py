'''Desafio 044

elabore um programa que calcule o valor a ser pago por um produto considerando
o seu preço normal e condição de pagamento

    A vista dinheiro cheque 10%
    a vista no cartão 5%
    2x no cartão 0%
    3x ou mais no cartão 20%'''

valor=int(input('Quanto custa o produto? R$'))
print('Digite [1]Á VISTA\nDigite [2]Á VISTA NO CARTÃO\nDigite [3] 2x NO CARTÃO\nDigite [4] 3x ou mais no cartão')
x=int(input('Voce quer pagar de que forma? '))
            
if x==1:
    print(f'Voce vai pagar no total um valor de R${valor-(valor*0.1)}')
elif x==2:
    print(f'Voce vai pagar no total um valor de R${valor-(valor*0.05)}')
elif x==3:
    print(f'Voce vai pagar no total um valor de R${valor}')
elif x==4:
    print(f'Voce vai pagar no total um valor de R${valor+(valor*0.2)}')

