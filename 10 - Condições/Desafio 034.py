"""DESAFIO 034

PERGUNTE O SALARIO DE UM FUNCIONARIO E CALCULE O VALOR DO SEU AUMENTO

PARA SALARIOS SUPERIOES A R$1.250,00 CALCULE UM AUMENTO DE 10%

PARA INFERIOES OU IGUAIS, O AUMENTO É DE 15%"""

sal=float(input('Qual seu salário? '))
print('Você ganhou um aumento parabéns!\n\n')

if sal>1250.0:
    print('Voce recebeu um aumento de 10%\nParabéns!\nAgora seu Salário é {}'.format(sal*0.1+sal))
else:
    print('Voce recebeu um aumento de 15%\nParabéns!\nAgora seu  Salário é {}'.format(sal*0.15+sal))
