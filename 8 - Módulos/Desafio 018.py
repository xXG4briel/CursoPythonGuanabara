import math
seno=int(input('Digite um valor para descobrir seu seno: '))
cos= int(input('Digite um valor para descobrir seu cosseno: '))
tang=int(input('digite um valor e te mostrarei a  tangente dele:'))
rs=math.sin(seno)
rcos=math.cos(cos)
rtamg=math.tan(tang)
print('seno={:.2f} cosseno={:.2f} tangente={:.2f}'.format(rs,rcos,rtamg))
