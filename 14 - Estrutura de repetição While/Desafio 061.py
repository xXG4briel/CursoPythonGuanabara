primeiro_termo=int(input('Digite o primeiro termo: '))
razao=int(input('Digite a razão: '))
cont=0
var = bool(1)
quest=''

while var == True:
    print(primeiro_termo, end=' ')
    primeiro_termo+=razao
    cont+=1
    if cont==10:
        print('Acabou !!!!')
        var=0 #Fecha o programa
        
        
