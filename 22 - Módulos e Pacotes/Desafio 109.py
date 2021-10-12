from ex109 import moeda

p = float(input('Valor:'))
print(moeda.aumentar(p,78,True))
print(moeda.diminuir(p,65,True))
print(moeda.metade(p))
print(moeda.dobro(p))

def aumentar(num,aut=10,sit=False):
    x = (num + (num*aut/100))
    if sit:
        x = str(x).replace('.', ',')
        num = str(num).replace('.',',')

    return f'Aumentando {aut}% de R${num} temos, \033[0:32mR${x}\033[m'

def diminuir(num,aut=10,sit=False):
    x = (num - (num * aut / 100))

    if sit:
        x = str(x).replace('.', ',')
        num = str(num).replace('.', ',')

    return f'Diminuindo {aut}% de R${num} temos, \033[0:32mR${x}\033[m'

def dobro(num,sit=False):
    x = (num * 2)
    if sit:
        x = str(x).replace('.', ',')
        num = str(num).replace(',','.')
    return f'O Dobro de R${num} é \033[0:32mR${x}\033[m'

def metade(num,sit=False):
    x = (num / 2)
    if sit:
        x = str(x).replace('.', ',')
        num=str(num).replace('.',',')
    return f'A metade de R${num} é \033[0:32mR${x}\033[m'
