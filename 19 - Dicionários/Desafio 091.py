from random import randint
from time import sleep
lista = []
lista_organizada = []
lista_organizada_jogador = []
cont = maior = 0
dicio = {'Jogador1': randint(1,6) , 'Jogador2' : randint(1,6),
         'Jogador3' : randint(1,6),'Jogador4' : randint(1,6)} # 4 JOGADORES COM VALORES ALEÁTORIOS
lista.append(dicio.copy())
for x in lista:
    for v,k in x.items():
        if len(lista_organizada) == 0 or k > lista_organizada[-1]:
            lista_organizada.append(k)
            lista_organizada_jogador.append(v)
        else:
            for posi in range(len(lista_organizada)):
                if k  <= lista_organizada[posi]:
                    lista_organizada.insert(posi, k)
                    lista_organizada_jogador.insert(posi,v)
                    break
        print(f'{v} tirou {k} no dado')
        sleep(0.5)
print('\033[0:32m{}\n\033[0:30m{:^45}'.format('-'*45,'== RANKING  DOS JOGADORES =='))
for i in range(len(lista_organizada)-1,-1,-1):
    cont+=1
    print(f'{cont:>8}ª Lugar - {lista_organizada_jogador[i]} com {lista_organizada[i]} dados')
