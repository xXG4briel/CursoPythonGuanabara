palavras = ('python','linguagem','cobra','java','cafe',)
palavra = ' '
vogais = 'aeiou'
for i in range(len(palavras)):
    palavra=palavras[i]
    print(palavra, end=' ')
    for c in range(len(palavra)):
        if c==0:
            print(f'tem as vogais  ->', end=' ')
        if palavra[c] in 'aeiou':
            print(palavra[c], end=' ')
    print('')
    
    
                
            
    

