from utilidadesCeV.dado import leia_dinheiro

leia_dinheiro()

def leia_dinheiro(aut=10,dim=10):
    while True:
        var = str(input('Digite um valor: ')).replace(',','.')
        try:
            var = float(var)
            print(f'{"-"*45}\n{"Resumo valor":^45}\n{"-"*45}')
            break
        except:
            print('\033[0:31mErro tente novamente\033[m')
    text = ['Preço analisado: ', 'Dobro do preço: ', 'Metade do preço: ', f'{aut}% de aumento: ',f'{dim}% de redução: ']
    lista = [var , var*2, var/2 , var+var*aut/100, var-var*dim/100]
    for k in range(5):
        print(f'* {text[k]:<35}R$ {lista[k]:.2f}')
