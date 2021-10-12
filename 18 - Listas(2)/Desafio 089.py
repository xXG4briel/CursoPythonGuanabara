lista = []
nota = []
med = 0
while True:
    nota.append(str(input('Digite seu nome: ')))
    nota.append(int(input('Digite sua nota: ')))
    nota.append(int(input('Digite sua nota: ')))
    lista.append(nota[:])
    nota.clear()
    stop =' '
    while stop not in 'NS':
        stop = str(input('Quer continuar ? [S/N] ')).upper().strip()
    if stop in 'N':
        break
print('{}\n{:<10}{:^10}{:^10}{:>10}'.format('-'*40,'Aluno','Nota1','Nota2','Média'))
for i in range(len(lista)):
    for  c in range(3):
        if c==0:
            print(f'{lista[i][c]:<11}',end='')
        elif c == 1:
            med+=lista[i][c]
            print(f'{lista[i][c]:^10}',end=' ')
        elif c == 2:
            med+=lista[i][c]  ; med/=2
            if med <=6:
                print(f'{lista[i][c]:^10}\033[0:31m{med:^10}\033[0:30m',end='\n')
            else:
                print(f'{lista[i][c]:^10}\033[0:32m{med:^10}\033[0:30m', end='\n')
            med=0
print('-'*40)

name = str(input('Quer ver os dados de quem? '))
for i in range(len(lista)):
    if name in lista[i]:
        print('{:<10}{:^10}'.format('Nota1','Nota2'))
        for y,x in enumerate(lista[i]):
            if y > 0:
                print(f'{x:<10}', end='')
            elif y>1:
                print(f'{x:>10}', end='')
                break
