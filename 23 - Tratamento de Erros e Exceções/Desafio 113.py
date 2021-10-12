def leia_int():
    while True:
        var = bool(False)
        varint = input('Digite um inteiro: ').strip()

        try:
            varint = int(varint)
            var = True
            return varint
        except:
            print('\033[0:31mERRO: por favor, digite um número inteiro válido.\033[m')

        if var :
            break


def leia_float():
    while True:
        varfloat = input('Digite um Real: ').strip().replace(',','.')
        var = bool(False)
        try:
            varfloat = float(varfloat)
            var = True
            return varfloat
        except:
            print('\033[0:31mERRO: por favor, digite um número inteiro válido.\033[m')
        if var:
            break

x = leia_int()
y = leia_float()

print(f'Os valores digitados foram {x} e {y}')
