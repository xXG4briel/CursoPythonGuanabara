'''69 crie um programa que leia a idade e sexo de varias pessoas
a cada pessoa cadastrada, o programa deverá perguntar se o usuário 
quer ou não continuar. No final, mostre:

A quantas pessoas tem  mais de 18 anos
b Quantos homens foram cadastrados
C Quantas mulheres tem menos de 20 anos'''

maior = man  = mulher_nova = idade = continuar = 0
sexo = continuar = ''

while True:
    idade = int(input('Digite sua idade: '))

    if idade>=18:
        maior+=1 # maiores de idade
            
    sexo=str(input('Digite seu sexo[M/F] ')).upper().strip()
    while  sexo not in 'MmFf':
        sexo=str(input('Digite seu sexo[M/F] '))
    
    if idade < 20 and sexo in 'Ff':
        mulher_nova+=1 #  quantas mulheres tem menos de 20

    if sexo in'Mm':
        man+=1 # quantos homens forão cadastrados
        
    continuar =  str(input('Quer parar ? [S/N]__')).upper().strip()
    print('-'*25,'')
    if continuar in 'Ss':
        break
print(f'A tem {maior} pessoas maiores de 18 anos\nB Tem {man} homens cadastrados\nC Tem {mulher_nova} mulheres com menos de 20 anos')
