'''faça um programa que faça a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário. O programa será interrompido  quando o  número 
solicitado for negativo
'''
while True:
    print('-'*20,'\n')
    tab = int(input('Digite um valor:  '))
    if tab<0:
        print('-'*25,'\nOperação finalizada')
        break
    for i in range(1,11):
        print(f'{tab} x {i} = {tab*i}')
    print(' ')
    
