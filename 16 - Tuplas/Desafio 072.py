num =('zero','um','dois','tres','quatro','cinco','seis','sete',
      'oito','nove','dez','onze','doze','treze','cartoze','quinze'
      ,'dezeisseis','dezessete','dezoito','dezenove','vinte')
while True:
    num_pessoa = 0
    while num_pessoa < 21 :
        print('-'*25)
        num_pessoa = int(input('Digite um número de 0 a 20: '))
        if num_pessoa < 0 :
            break
        print(f'você digitou o número {num[num_pessoa]}')
    if num_pessoa < 0:
        break

