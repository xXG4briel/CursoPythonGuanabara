cont9 =  posi = 0
var=True
par = [0,0,0,0]
var1 =int(input('Digite um número: '))
var2 =int(input('Digite outro número: '))
var3 =int(input('Digite mais um número: '))
var4 =int(input('Digite o ultimo número: '))
tupla = (var1,var2,var3,var4)
print(f'Você  digitou os valores {tupla}', end='')

for i in range(len(tupla)):
    if tupla[i] == 9:
        cont9+=1
    if i == len(tupla)-1:
        print(f'\nO valor 9 apareceu {cont9} vezes',end='')
    if tupla[i] ==3 and var == True:
        posi = i
        print(f'\nO valor 3 apareceu na {posi+1}ª posição')
        var=False
print('Os valores pares  digitados foram ', end='')
for x in range(len(tupla)):
    if tupla[x] % 2 == 0:
        print(tupla[x],end=' ')

    







