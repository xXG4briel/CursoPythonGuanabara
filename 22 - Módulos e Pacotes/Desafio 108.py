def aumentar(num,aut=10):
    x = (num + (num*aut/100))
    x = str(x).replace('.', ',')

    num = str(num).replace('.',',')

    return f'Aumentando {aut}% de R${num} temos, \033[0:32mR${x}\033[m'

def diminuir(num,aut=10):
    x = (num - (num * aut / 100))
    x = str(x).replace('.', ',')

    num = str(num).replace('.', ',')

    return f'Diminuindo {aut}% de R${num} temos, \033[0:32mR${x}\033[m'

def dobro(num):
    x = (num * 2)
    x = str(x).replace('.', ',')
    num = str(num).replace(',','.')
    return f'O Dobro de R${num} é \033[0:32mR${x}\033[m'

def metade(num):
    x = (num / 2)
    x = str(x).replace('.', ',')
    num=str(num).replace('.',',')
    return f'A metade de R${num} é \033[0:32mR${x}\033[m'


from ex107 import moeda

while True:
    x = str(input('Digite um valor: ')).strip()
    x = x.replace(',','.')
    if x[0] != 0 :
        x = float(x)
        if x > 0:
            x = float(x)
            break
    else:
        print('\033[0:31mErro! digite um número valido\033[m')

print(moeda.aumentar(x))
print(moeda.diminuir(x))
print(moeda.dobro(x))
print(moeda.metade(x))
