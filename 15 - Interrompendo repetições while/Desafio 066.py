'''crie um programa que leia varios  numeros inteiros 
pelo teclado. O programa só vai parar quando o 
usuário digitar o valor 999, que é a condição de parada
mostre no final a soma e quantos números foram digitados
'''

soma = num = cont = 0
while True:
    num=int(input('Digite um número: '))
    if num==999:
        break
    soma+=num
    cont+=1
print(f'A soma total foi {soma} com um total de {cont} digitos(tirando o 999)')
