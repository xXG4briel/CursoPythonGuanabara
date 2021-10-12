'''Crie um programa que simule o funcionamento de um caixa eletrônioc. No início,
pergunte ao  usuário qual será o valor a ser sacado (número interio) e o ]
programa vai informar quantas cédulas de cada valor  serão entregues.'''

din = int(input('Digite quanto deseja sacar:R$'))

while True:
    var = din //50
    din-=(var*50)

    var2= din//20
    din-=(var2*20)

    var3 = din//10
    din-=(var3*10)

    var4 = din//1
    break
print(f'Cédulas de 50 reais: {var}\nCédulas de 20 reais: {var2}\nCédulas de 10 reais: {var3}\nCédulas de 1 real: {var4}')
