from random import randint
lista=[]
num = int(input('Quantos palpites? '))
for i in range(num):
    randomizar = [randint(1,60),randint(1,60),randint(1,60),randint(1,60),randint(1,60),randint(1,60),]
    lista.append(randomizar[:])
for y,x in enumerate(lista):
    print(f'{y+1:3}ª palpite = {x}')
