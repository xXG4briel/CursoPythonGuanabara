soma=num=cont=0

while num!=999:
    num=int(input('Digite um número: '))
    if num !=999:
        soma=soma+num
        cont+=1
print(f'voce digitou {cont} vezes e a soma foi {soma}')
