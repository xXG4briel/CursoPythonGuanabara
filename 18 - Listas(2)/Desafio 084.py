lista = []
nome_peso = []
while  True:

    stop=str(input('Quer continuar? [S/N] ')).upper().strip()
    if stop in 'N':
        break
print(f'Tem {len(lista)} pessoas cadastradas')
