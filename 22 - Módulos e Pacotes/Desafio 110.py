def resumo(num=0,aut=10,dim=10):
    lista =  [num*1.0,num*2.0,num/2,num+num*aut/100,num-num*aut/100]

    for c in range(5):
        lista[c] = str(lista[c]).replace('.',',')
        lista[c] = "R$" + lista[c]

    """
    :param num: Informar número a ser cálculado
    :param aut: informar porc valor que vai ser aumentado
    :param dim: Informar porc valor que vai ser diminuido
    :return: retorna o valor
    """
    print('{}\n{:^45}\n{}'.format('-'*45,'Resumo de valor','-'*45))
    print(f'Preço analisado:   {lista[0]:^35}')
    print(f'Dobro do preço:    {lista[1]:^35}')
    print(f'Metade do preço:   {lista[2]:^35}')
    print(f'{aut}% de aumento:    {lista[3]:^35}')
    print(f'{dim}% de redução:    {lista[4]:^35}')


from ex110 import resumo

p = float(input('Digite um valor: '))
resumo(p, 75,82)
