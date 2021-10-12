'''leia 5 pesos de 5 pessoas
e no final mostre qual foi o  maior e o menor peso  lidas'''

maior=0
menor=0

for i in range(5):
    peso = float(input('Digite seu peso: '))
    if i==0:
        menor=peso
        maior=peso
    else:
        if peso > maior:
            maior=peso
        if peso < menor:
            menor=peso
print(f'\nO maior peso foi {maior:.2f}kg\nO menor peso foi {menor:.2f}kg')
    
