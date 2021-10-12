#calcule a soma entre todos os números impares que são múltiplos de trêss e que esteja entre 1 e 500


soma=  int()
cont=int()
for i in range(3,500,2):
    if (i%3)==0:
        cont+=1
        soma=soma+i

print(f'{cont} valores \nE a soma de {soma}')
    
