'''faça um programa que jogue par ou ímpar com o computador. O jogo só  sera
interrompido quando  o jogador  perder mostrando o total o total de vitórias
consecutivas que ele conquistou no final do jogo'''

from random import randint

chances = num = num_maquina = escolha_jogador = escolha_maquina = 0

while True:
    escolha_maquina ='P'
    num = int(input('Digite um número: '))
    escolha_jogador = str(input('[P/I] Pár ou Ímpar:  ')).upper().strip()

    if escolha_jogador == 'P':
        escolha_maquina = 'I'
        
    num_maquina = randint(0,10)
    print(f'Voce digitou {num} e o computador escolheu {num_maquina}.\nO total foi {num_maquina+num}')

    if escolha_jogador ==  'P' and (num+num_maquina)%2 != 0:
        print(f'Voce perdeu :(\nVoce {chances}x')
        break
    if escolha_jogador ==  'I' and (num+num_maquina)%2 == 0:
        print(f'Voce perdeu :(\nVoce {chances}x')
        break
    print('Você venceu !!!!!\n')
    chances+=1
        

