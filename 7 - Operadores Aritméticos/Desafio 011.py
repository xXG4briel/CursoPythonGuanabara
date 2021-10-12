L=int(input('Qual a Largura da sua parede? '))
H=int(input('Qual a altura da sua parede? '))
metq=L*H
print(metq,'m²')
print('Supondo que cada litro de tinta pinte 2m²')
print('Voce precisaria de um total de {} litros\npara pintar sua parede'.format(metq/2))
