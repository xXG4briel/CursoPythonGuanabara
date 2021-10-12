def leiaInt():
    contnum = contStr= 0
    x = input('Digite um valor: ')
    for c in x:
        if c not  in '0123456789':
            contStr+=1
        else:
            contnum+=1
    if contStr == 0 and contnum > 0 :
        return 'É um número'
    else:
        return 'Não é um número'

print(leiaInt())
