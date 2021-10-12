# leia seis números inteiros e mostre a soma apénas daqueles que são pares 


soma=int()
for i in range(6):
    x=int(input(f'Digite o {i+1} valor número: '))
    if x%2==0:
        soma+=x
print(f'A soma é {soma}')
        
