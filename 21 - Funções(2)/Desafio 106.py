from time import sleep
def main():
    while True:
        sap = 'Sistema de ajuda pyhelp'.upper()
        amc = 'Acessando o manual do comando'
        func = input('\033[0:42m'+ f'{"-"*len(sap)}\n{sap}\n{"-"*len(sap)}\n\033[0:30mFunção ou Biblioteca >')
        amc = amc + f" '{func}'"  # para pegar a fução ou biblioteca digitada
        sleep(0.5)
        print('\033[0:46m' + f'{"-"*len(amc)}\n{amc}\n{"-"*len(amc)}')
        sleep(0.5)
        print('\033[0:30m\033[7:30m', ) # para forçar a cor preto
        help(func)
main()
