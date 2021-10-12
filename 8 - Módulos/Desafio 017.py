import math
cato=int(input('Digite um valor para cateto oposto: '))
cata= int(input('Digite um valor para o cateto adjacente: '))
hip=math.hypot(cato,cata)
print('     /|\n    / |\n   /  |CO={}\n  /)  |\n   CA={}'.format(cato, cata))
print('\n\n\n')
print('o valor da hipotenusa equivale a {:.1f}'.format(hip))
