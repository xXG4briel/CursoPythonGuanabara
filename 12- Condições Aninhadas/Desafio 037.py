'''Desafio 037

Escreva um programa que leia um número inteiro qualquer e peça para o usuário
escolher qual será a base de conversão:

    1 binário
    2-octal
    3-hexadecimal'''    
while  0==0:
    print('\n')
    y=int(input('Digite um valor: '))
    print(''''Conversor
    [1] para Binario
    [2] para Octal
    [3] para hexadecimal''')

    x=int(input('Digite sua escolha: '))
    if x==3:
        z=hex(y)
        z=z.replace('0x', '')
        print(z)
    elif x==2:
        z= oct(y)
        z= z.replace('0o', '')
        print(z)
    elif x==1:
        z=bin(y)
        z=z.replace('0b','')
        print(z)
    else:
        print('Valor Não encontrado\nTente Novamente\n\n')
