cont = maior = menor = media = num = soma = var = 0
cond = bool(False)

while cond != True:
    num= int(input('Digite um número:  '))

    soma+=num
    media=soma
    cont+=1
    
    if cont == 0:
        maior = num
        menor = num
        
    if num > maior:
        maior=num
        
    if num<menor:
        menor=num
        
    var = int(input('[1] Para fechar o programa\n[2]Para continuar a execução\nDigite: '))

    if var == 1:
        cond=True
print(f'a soma foi {soma} e a média {media/cont}')
        
    
