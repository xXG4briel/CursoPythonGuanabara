from random import randint

tupla = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
maior = menor = 0
print(tupla)
for i in range (len(tupla)):
    if i==0 or tupla[i] > maior:
        maior = tupla[i]
    if i==0 or tupla[i] < menor:
        menor=tupla[i]
print(f'O maior valor foi {maior}\nO menor valor foi {menor}')

