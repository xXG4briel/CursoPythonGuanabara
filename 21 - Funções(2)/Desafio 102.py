def fatorial(num=0,sit=False):
    valor = 1
    if sit==True:
        for i in range(num,0,-1):
            if i==1:
                print(f'{i} = ', end='')
            else:
                print(f'{i} x ', end='')
            valor*=i
        return f'\033[1:32m{valor}'
    else:
        for i in range(num,0,-1):
            valor*=i
        return f'O fatorial de {num} é \033[1:32m{valor}'


print(fatorial(15,sit=1))
