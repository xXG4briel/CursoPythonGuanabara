##Desafio 027

"""Faça um programa que leia o nome completo de uma pessoa, mostrando
em seguida o primeiro e último nome separadamente.

    Ex:Ana Maria de Souza
    primeiro=Ana
    último=Souza
    """
nm=str(input('Digite seu nome COMPLETO: ')).strip().title()
sep=nm.split()
ftnm=sep[0]
end=sep[1]
print('Primeiro nome {}\n Segundo Nome {}'.format(ftnm,end))
