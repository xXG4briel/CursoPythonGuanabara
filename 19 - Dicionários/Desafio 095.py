dicio = {}
lista = []
while True:
    soma=0
    dicio['nome']  = str(input('Nome do Jogador: '))
    dicio['jogos'] = int(input('Quantos partidas jogou? '))
    for x in range(dicio['jogos']):
        if x == 0:
            lista_gols = list(range(0,dicio['jogos']))
            dicio['gols'] = lista_gols.copy()
        dicio['gols'][x] = int(input(f'\tQuantos gols no jogo {x+1}: '))
        soma += dicio['gols'][x]
    dicio['total'] =  soma
    lista.append(dicio.copy())
    stop  = ' '
    while stop not in 'NS':
        stop = str(input('Quer continuar ? [S/N] ')).upper().strip()
    if stop in 'N':
        formata = len(dicio['gols'])
        print('{:^3} {:<11} {}{}  {}'.format('cod', 'nome', 'gols', ' ' * ((formata + 1) * 2), 'total'))
        for v, k in enumerate(lista):
            print('{:^3} {:<11} {}  {}'.format(v, k["nome"], k["gols"][:], k["total"]))
        break
num = 0
while num != 999:
    print('-' * 30)
    num = int(input('\nMostar dados de qual jogador? (999 para parar) '))
    for y,x in enumerate(lista[num].values()):
        if y==2:
            for h in range(len(x)):
                print(f'na partida {h+1} fez {x[h]} gols')
print("encerrado")
