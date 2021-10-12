def aerea():
    print('Controle de Terrenos\n{}'.format('-' * 30))
    lar = float(input('Largura (m): '))
    comp = float(input('Comprimento (m): '))
    print(f'A área de um terreno é {lar}m x {comp}m é de {lar*comp:.2f}m²')
aerea()
