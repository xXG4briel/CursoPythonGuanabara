barato = produto_barato = caro = gasto = nome_produto = status = produto = 0

while True:
    nome_produto = str(input('Digite o nome do produto: ')).capitalize().strip()

    produto = float(input('Quanto custa o produto: '))
    if gasto==0:
        barato = produto
        produto_barato = nome_produto

    if produto < barato : # pega o nome do produto mais barato
        barato = produto
        produto_barato = nome_produto
        
    if produto > 1000: 
        caro+=1
    
    gasto+=produto # soma  os gastos total
    print('-'*20)
    status = str(input('Parar?\n[S/N] '))
    
    if status in 'Ss':
        break

print(f'''O total das compras foi R${gasto:.2f}
\nO produto mais barato foi  '{produto_barato}' custando R$ {barato:.2f}
\nVoce tem {caro} produtos que valem mais de R$1000''')
