#leia um número inteiro e diga se ele é ou não um número primo

num = int(input('Digite um número: '))
cont=int()

for i in range(1,num+1):
    if num % i == 0:
        cont+=1
        print(f'{i:2}', end=' → ')
    else:
        print(f'{i:2}',end=' → ')
    if i% 10 == 0 :
        print(' ')
print(('É primo')if  cont==2 else('Não é primo'))





    
