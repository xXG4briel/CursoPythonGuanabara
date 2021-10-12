'''Desafio 040

Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando
uma mensagem no final, de acordo com a média atingida:
    MEDIA ABAIXO DE 5: REPROVADO
    
    MEDIA ENTRE 5 E 6.9: RECUPERAÇÃO
    
    MÉDIA 7 OU SUPERIOR: APROVADO'''
x=float(input('Qual foi a primeira nota? '))
x=(x+float(input('Qual foi a primeira nota? ')))/2
#y=float(input('Qual foi a segunda nota? '))+x
print(x)
if x>=5 and x<=6.9:
    print('Recuperação')
elif x<5:
    print('Reprovado')
elif x>6.9:
    print('Aprovado')
