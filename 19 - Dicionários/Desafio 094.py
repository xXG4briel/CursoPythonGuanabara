lista = []
dicio = {}
idade = 0
while True:
    dicio['nome'] = str(input('\nNome: ')).capitalize().strip()
    dicio['Sexo'] = ' '
    while  dicio['Sexo'] not  in 'MF':
        dicio['Sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
    dicio['idade'] = int(input('Idade: '))
    idade+=dicio['idade']
    lista.append(dicio.copy())
    stop = ' '
    while stop not in 'NS':
        stop = str(input('Continuar ? [S/N] ')).upper().strip()[0]
    if stop in 'N':
        break
idade = idade /  len(lista)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas\nB) A média de idade é de {idade}')
print(f'C) As mulheres cadastradas foram ',end='')
for list in lista:
    if list["Sexo"] in 'F':
        print(list["nome"], end=' ')
print('\nD) Lista das pessoas que estão acima da média: ')
for v in lista:
    if v['idade'] > idade:
        for k,v in v.items():
            print(f'{k}={v}; ', end='')
