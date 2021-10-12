from random import randint
lista = []
def sorteia():
    for i in range(6):
        lista.append(randint(1, 10))
sorteia()

def par(lista):
    soma = 0
    for i in lista:
        if i % 2 ==0:
            soma+=i
    print(f'Sorteando 5 valores da lista {lista} PRONTO!\nSomando os valores pares de {lista}, temos  {soma} ')
par(lista)
