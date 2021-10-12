from datetime import datetime
ano = datetime.today().year # ano

dicio ={}
lista=[]
dicio['nome'] = str(input('Nome: ')).capitalize().strip()
dicio['idade'] = int(input('Digite seu ano de nascimento: ')) ; dicio['idade'] = ano - dicio['idade'] # converte para a idade
dicio['ctps'] = int(input('Carteira de trabalho: '))
if dicio['ctps'] != 0:
    dicio['contratação'] =  int(input('Ano de contratação: '))
    dicio['salario'] = float(input('Salário: R$'))
    dicio['aposentadoria']  = dicio['idade'] + 30
lista.append(dicio.copy())
print('--'*50)
for x in lista:
    for v,k in  x.items():
        print(f'{v} tem o valor {k}')
