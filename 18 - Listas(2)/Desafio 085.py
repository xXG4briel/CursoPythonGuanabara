lista = [[],[],[]] # 0 num, 1 par , 2 impar

for i in range(7):
    num= int(input('Digite um valor: '))
    lista[0].append(num)
    if num % 2 == 0:
        lista[1].append(num)
    else:
        lista[2].append(num)
print(f'Valores digitados {lista[0]}\nValores ímpares {lista[2]}\nValores pares {lista[1]}')
        
