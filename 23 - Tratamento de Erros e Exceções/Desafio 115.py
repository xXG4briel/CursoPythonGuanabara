from ex115 import cadastros
from ex115 import menu
from time import sleep
choose = 0
while choose != 3:
    try:
        menu.main()
        choose = int(input('Sua opção: '))
        if choose == 1:
            menu.see()
        elif choose == 2:
            cadastros.criar()
    except:
        print(f'\033[0:31mERRO Tente novamente\033[m')
print('Encerrando...')
sleep(1)
print('Volte mais tarde')


#

def criar():
    global var
    try:
        arquivo = open('cadastro.txt', 'r')  # Abra o arquivo (leitura)
        conteudo = arquivo.readlines()
        name = str(input('\033[0:35mNome: '))
        var = True
    except:
        print('Arquivo inexistente certifiquesse de criar-lo  e reinicie o programa')
        var = False


    while True:
        if not var:
            break
        year = str(input('\033[0:35mIdade: \033[m'))
        try:
            year = int(year)
            conteudo.append(f'{name:<25}{year}\n')  # insira seu conteúdo
            break
        except:
            print('\033[0:31mERRO !!!Digite uma idade válida\033[m\n')



    arquivo = open('cadastro.txt', 'w')  # Abre novamente o arquivo (escrita)
    arquivo.writelines(conteudo)  # escreva o conteúdo criado anteriormente nele.

    arquivo.close()

#

def main():
    print(f'{"-"*35}\n{"MENU PRINCIPAL":^35}\n{"-"*35}')

    print(f'\033[0:32m1 - \033[0:35mVer pessoas cadastradas \n\033[0:32m2 - \033[0:35mCadastrar nova Pessoa\n\033[0:32m3 - \033[0:35mSair do Sistema\033[m\n{"-"*35}')

def see():
    print(f'\n{"-"*35}\n{"Pessoas Cadastradas":^35}\n{"-" * 35}')
    global read
    read = bool(False)

    try:
        arquivo = open("cadastro.txt", "r").read()
        read = True
    except:
        arquivo = open("cadastro.txt", 'w')
        read = False
    print(f'{(arquivo) if read else ("Impossível ler o arquivo feche o programa")}')

