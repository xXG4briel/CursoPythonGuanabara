"""Desafio 035


Densevolva um programa que leia o comprimeto de 3 retas e
mostre se é possivel fazer um triangulo ou nao"""


from random import randint
A=randint(1,50)
B=randint(1,50)
C=randint(1,50)
print('A={}\nB={}\nC={}'.format(A,B,C))
if A>B and A>C:
    if A>B+C:
       print('Forma um triangulo')
    if B>A and B>C:
     if B>A+C:
       print('Forma um triangulo')
    if C>B and C>A:
        if C<A+B:
         print('Forma um triangulo')
    else:
        print('não forma')

