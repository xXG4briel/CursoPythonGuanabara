###Desafio 042

'''refaça o desafio 035 dos triângulos, acresntando o recurso de mostrar que tipo de
triângulo será formado:
    ESQUILÁTERO TODOS OS LADOS IGUAIS
    ISÓSCELES: DOIS LADOS IGUAIS
    ESCALENO: TODOS OS LADOS DIFERENTES'''
tri=0
while tri==0:
    x= float(input('Digite um valor para a reta'))
    y= float(input('Digite outro valor para outra reta'))
    z= float(input('Digite um valor para a ultima reta'))
    if x<y+z and y<x+z and z<x+y:
        if x==y and y==z and z==x:
            forma='Equilatero'
        elif x==y or y==z or z==x:
            forma='Isósceles'
        else:
            forma='Escaleno'
        print('\n\nForma um triângulo {}'.format(forma))
        print('\n'*3)
    else:
        print('Não forma um triângulo')
        print('\n'*3)

