dicio = {} ; lista = [] # Vars
dicio['Nome'] = str(input('Nome: '))
dicio['Média'] = float(input(f'Média de {dicio["Nome"]}: '))
dicio['Situação'] = ('Aprovado') if dicio['Média'] >= 6 else('Recuperação')
lista.append(dicio.copy())
print('-'*40,'\033[0:34m')
for x in lista:
        for i,k in x.items():
                print(f'{i} é igual a {k}')
