"""DESAFIO 033

coloque um 3 valores e me mostre o maior menor """
w=0
while w==0:
    print('\n{:-^80}\n{:^80}\n{:-^80}\n\n\n'.format('-','Digite 3 valores e mostrei o maior,mediano e menor','-'))
    X=int(input('Digite um numero: '))
    Y=int(input('\nAgora outro numero: '))
    Z=int(input('\nMais um numero: '))

    if X>Y>Z or X>Z>Y:
        print('{} foi o maior numero'.format(X))
    elif Y>X>Z or Y>Z>X:
        print('{} foi o maior numero'.format(Y))
    elif Z>X>Y or Z>Y>X:
        print('{} foi o maior numero'.format(Z))
    if Y<X<Z or Z<X<Y :
        print('{} é o numero do meio'.format(X))
    elif X<Y<Z or Z<Y<X:
        print('{} é o número do meio'.format(Y))
    elif X<Z<Y or Y<Z<X:
        print('{} é o numero do meio'.format(Z))
    if X<Y<Z or X<Z<Y:
        print('{} foi o menor numero'.format(X))
    elif Y<X<Z or Y<Z<X:
        print('{} foi o menor numero'.format(Y))
    elif Z<Y<X or Z<X<Y:
        print('{} foi o menor numero'.format(Z))
    a=str(input('\n\nQuer fechar o programa? ')).upper()
    if a=='SIM' or 'S':
        w=w+1
    else:
        print('\n')
else:
    print('Programa encerrado')
