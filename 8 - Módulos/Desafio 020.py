import random
a='Joao,Marcelo,Luana e Alice'
b='Lucas,Matheus,Bruna e Julia'
c='Jose,Gabriela,Gabrielle e Leticia'
d='Igor,Alex,Sabrina e Martha'
ra=random.randint(1,4)
if ra==1:
    print('Vem apresentar o trabalho {}'.format(a))
if ra==2:
    print('Venham apresentar o trabalho {}'.format(b))
if ra==3:
    print('Venham apresentar o trabalho {}'.format(c))
if ra==4:
    print('Venham apresentar o trabalho {}'.format(d))
