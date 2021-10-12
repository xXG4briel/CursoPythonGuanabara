
def notas(*num,sit = False):
    dicio = {}
    result = ' '
    dicio['Notas'] = num
    dicio['Maior nota'] = max(num)
    dicio['Menor  nota'] = min(num)
    soma = 0
    for c in num:
        soma+=c
    dicio['Média'] = soma / len(num)
    if sit == True:
        if dicio['Média'] <=5 :
            result = 'Ruim'
        elif dicio['Média'] <=6.5:
            result = 'Razoavél'
        elif dicio['Média'] <=8:
            result='Bom'
        else:
            result='Ótimo'
        dicio['Situação'] = result
    return dicio
print(f'{notas(5,6,10,10,sit = True)}')
