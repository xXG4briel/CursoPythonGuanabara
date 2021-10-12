print('Olá, hoje vou te ajudar a calcular a sua média de um bimestre')
medi=int(input('Qual a sua nota na primeira prova? '))
print('Voce tirou na primeira avaliação {}'.format(medi))
med2=int(input('E na segunda? '))
print('Voce tirou na segunda avaliação {}'.format(med2))
print('............')
print('............')
print('............')
print('............')
resultado=((medi+med2)/2)
if resultado > 6:
    print('Nota Azul', resultado)
else:
    print('Nota Vermelha', resultado)
