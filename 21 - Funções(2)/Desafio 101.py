from datetime import datetime
data = datetime.today().year
def voto(nascimento):
    y = data - nascimento
    result  = ' '
    if y < 18:
        result = 'Negado '
        return result
    if 18 <= y < 65:
        result = 'Obrigatório'
        return  result
    else:
        result = 'Opcional'
        return result
nasci = int(input(f'{"-"*40}\n{"Digite seu ano de nascimento: "}'))
print(f' O seu voto é: {voto(nasci)}')
