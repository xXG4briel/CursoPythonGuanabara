#faça um porgrama que leia um número qualquer e mostre o seu fatorial

'''x=float(input('Digite um valor: '))
i=x

while i!=1:
    i-=1
    x=x*i      
print(x)'''

x=int(input('Digite um valor: '))
print(x, end=' - ')
for i in range(x,0,-1):
    if i<x:
        x=x*i
        print(i, end=' - ')
    
print(x)
