from time import sleep

def contador():
    print('-'*40,f'\nContagem de 1 até 10 de 1 em 1')
    for c in range(1,11):
        print(f'{c} ', end='')
        sleep(0.3)
    print('Fim')
    print('-' * 40, f'\nContagem de 10 até 0 de 2 em 2')
    for x in range(10, -1,-2):
        print(f'{x} ', end='')
        sleep(0.3)
    print('Fim')
    a= int(input('Agora é sua vez de personalizar a contagem!\nInício: '))
    b = int(input('Fim: '))
    c = int(input('Passo: '))
    print(f'Contagem de {a} até {b} pulando de {c} em {c}')
    if c==0:
        c=1
    if b > a:
        for z in range(a,b+1,c): # se b for maior
            print(f'{z} ',end='')
            sleep(0.2)
    if a > b:
        if c >0:
            for z in range(a,b-1,-c): # se b for menor
                print(f'{z} ',end='')
                sleep(0.2)
        else:
            for z in range(a,b-1,c): # se b for menor
                print(f'{z} ',end='')
                sleep(0.2)
    print('Fim')
contador()
