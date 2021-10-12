'''programa que leia o nome de nascimento de 7 pessoas
e mostre quantos ainda não atingiram a maioridade
e quantos já são maiores(21 anos)'''

contador_menor_idade=0

for i in range (7):
    idade=int(input('Digite  sua  data de nascimento: '))
    idade=2020-idade
    if idade < 22:
        contador_menor_idade+=1
print(f'Voce  possui {contador_menor_idade} menores de idade\nE {7-contador_menor_idade} Maiores de idade')

