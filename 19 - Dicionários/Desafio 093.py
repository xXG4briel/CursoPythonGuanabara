dicio = {}
soma = 0
dicio['nome']  = str(input('Nome do Jogador: '))
dicio['jogos'] = int(input('Quantos partidas jogou? '))
for x in range(dicio['jogos']):
    if x == 0:
        lista_gols = list(range(0,dicio['jogos']))
        dicio['gols'] = lista_gols.copy()
    dicio['gols'][x] = int(input(f'\tQuantos gols no jogo {x+1}: '))
    soma += dicio['gols'][x]
dicio['total'] =  soma
print(f'{"-"*40}\n{dicio}\n{"-"*40}')
for v,k in dicio.items():
    print(f'O campo {v} tem o valor {k}')
print(f' o Jogador {dicio["nome"]} jogou {dicio["jogos"]} partidas.')
for c,x in enumerate(dicio['gols']):
    print(f'\t=> Na partida {c+1}, fez {x} gols.')
print(f'foi um total de {dicio["total"]} gols')
