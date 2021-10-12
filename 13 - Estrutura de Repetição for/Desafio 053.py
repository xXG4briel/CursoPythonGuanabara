# leia um frase e diga se ela é um palíndromo desconsiderando os espaço

frase=str(input('Digite uma frase: ')).strip().upper().split()
frase=''.join(frase)

frase_contraria = frase # para pegar o mesmo tamanho
frase_contraria  = ''

for i in range(len(frase)-1,-1,-1):
    frase_contraria +=frase[i]
    ## usando fatiamento pode começar do final frase_contraria=frase[::-1]
print(f'A frase digita foi {frase}\nE a frase ao contrário é {frase_contraria}\n')
print('É palíndromo'if frase==frase_contraria else'Não é palíndromo')

