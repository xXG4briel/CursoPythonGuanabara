matriz = []
var = []
for i in range(3):
    var.append(int(input('Digite um valor: ')))
    var.append(int(input('Digite um valor: ')))
    var.append(int(input('Digite um valor: ')))
    matriz.append(var[:])
    var.clear()
for x in range(3):
    print(f'( {matriz[0][x]} )', end=' ')
print(' ')
for y in range(3):
    print(f'( {matriz[1][y]} )', end=' ')
print(' ')
for z in range(3):
    print(f'( {matriz[2][z]} )', end=' ')
