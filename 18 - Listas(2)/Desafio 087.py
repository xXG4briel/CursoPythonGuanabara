matriz = []
soma = soma3 = maior2 =0
var = [] #--> par
for i in range(3):
    var.append(int(input('Digite um valor: ')))
    var.append(int(input('Digite um valor: ')))
    var.append(int(input('Digite um valor: ')))
    matriz.append(var[:])
    for k in range(3): # vai somar os valores digitados caso seja  par
        if var[k] % 2 == 0:
            soma+=var[k]
    var.clear()
    
for x in range(3):
    print(f'( {matriz[0][x]} )',end ='')
print('')
for y in range(3):
    print(f'( {matriz[1][y]} )', end='')
    if y==0 or maior2 < matriz[1][y]:
        maior2 = matriz[1][y]
print('')
for z in range(3):
    print(f'( {matriz[2][z]} )', end='')
    soma3+=matriz[z][2]
    
print(f'\nA soma de todos valores pares digitados é {soma}\nA soma dos valores da terceira coluna é {soma3}\nE o maior valor da segunda linha é {maior2}')



    
