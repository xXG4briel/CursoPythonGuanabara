'''leia nome idade e sexo de 4 pessoas no final do programa mostre

a média de  idade  do grupoo

nome do homem mais velho

quantas mulheres tem menos de 20 anos'''

maior_idade_homem=0
nome_velho=''
média_idade=0
mulheres_novas=0
for i in range(2):

    print(f'\n{i+1}ª pessoa')
    nome=str(input('DIGITE SEU NOME: ')).strip().upper()
    idade=int(input('DIGITE SUA IDADE:'))
    sexo=str(input('M/F: ')).strip().upper()

    if sexo=='F' and idade < 21: ## mulheres menor  de 20 anos
        mulheres_novas+=1
    if sexo=='M' and idade > maior_idade_homem:
        maior_idade_homem=idade
        nome_velho=nome
        
    média_idade+=idade # MÉDIA DE IDADE

média_idade=média_idade/4

print(f'\nA média de idades é {média_idade:.2f} anos')
print(f'O homem mais velho se chama {nome_velho} e tem {maior_idade_homem} anos')
print(f'Tem {mulheres_novas} mulheres menores de idade')
