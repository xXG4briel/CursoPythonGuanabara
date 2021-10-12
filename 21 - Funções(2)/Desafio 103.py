def ficha(nome=False,gols=False):
    if nome== True and gols == True:
        return f'Seu nome é {name} e você marcou {num_gol} gol(s)'
    if nome == True and gols == False:
        return f'Seu nome é {name} e você marcou 0 gols'
    if nome == False and gols == True:
        return f'Seu nome é <Desconhecido> e vocÊ marcou {num_gol} gol(s)'
    if nome == False and gols== False:
        return f'Seu nome é <Desconhecido> e você marcou 0 gols'


var  = True
var2 = False
name = str(input('Nome: '))
gol = input('Gols: ')
if name == '':
    var = False
if gol != '':
    for c in gol:
        if c in '0123456789':
            num_gol = int(gol)
            var2=True
print(ficha(nome=var,gols=var2))
