var = cont = cont2 = termos2 =0
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite o segundo termo:  '))
termos =10
while var==False:
    cont += 1
    cont2 +=1
    print(f'{primeiro_termo}', end=' → ')
    primeiro_termo += razao
    if cont==termos:
        termos = int(input('Digite quantos termos voce quer: '))
        termos2 +=termos
        if termos==0:
            var=True
        if termos!=0:
            cont=0
print(f'Acabou\n\nVoce teve um total de {termos2+10} termos')
