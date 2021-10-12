print('**'*25,'\n\t\tFibonacci\n','**'*25)

num=cont=var = termo = numA = 0
numB = 1

while var  != True:
    if cont == 0:
            termo=int(input('Qual termos devo mostrar? '))
    num = numA+numB # vale  2
    print(f'{numA:4} + {numB:4} = {num:4}')
    numB=numA # VALE 1
    numA = num #vale 2

    
    cont+=1
    
    if cont == termo:
        var = 1
    
