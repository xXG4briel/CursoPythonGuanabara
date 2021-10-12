"""DESAFIO 032

ANO BISSEXTO"""

x=0
while x==0:
       print('{:_^80}\n\n{: ^70}\n{:_^80}'.format('','É bissexto ou não?',''))
       A=int(input('Digite um ano: '))
       div=A%4
       
       if div==0:
              print('{} é ano Bissexto'.format(A))

       else:
              print('{} é ano normal'.format(A))
       B=str(input('Voce que fechar o programa? ')).upper()
       if B=='SIM':
              x=x+1
       elif B=='S':
           x=x+1
       else:
              print('\n\n\n')
else:
       print('Programa finalizado')
