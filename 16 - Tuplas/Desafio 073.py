var = 0

brasileirao = ('Athletico Paranaense','Atlético-GO','Atlético-MG','Bahia',
               'Botafogo','Bragantino','Ceará','Corinthians','Coritiba','Flamengo',
               'Fluminense','Fortaleza','Goiás','Grêmio','Internacional','Palmeiras',
               'Santos','São Paulo','Sport','Vasco')

print('{}\n{: ^25}\n{}\n\n'.format('-'*25,'Colocados Brasileirao','-'*25))
for i in range(len(brasileirao)):
    print(f'{i+1} colocado {brasileirao[i]}' )
    if brasileirao[i] == 'Palmeiras':
        var = i
    if i ==19:
        print('\n','-'*35)
        for c in range (0,6):
            print(f'O {1+c} primeiro colocado foi {brasileirao[c]}')
            if c==5:
                print('\n','-'*35)
                for u in range(len(brasileirao)-1,15,-1):
                    print(f'Os 4 ultimos são = sendo o {u}ª {brasileirao[u]}')
print(f'\nO Palmeiras está na posição {var+1}')
