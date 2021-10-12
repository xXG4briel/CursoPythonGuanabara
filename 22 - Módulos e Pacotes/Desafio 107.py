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

x = int(input('Valor: '))
print(moeda.aumentar(x))
