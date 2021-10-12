'''faça um programa que mostre na tela uma contage regressiva para o
estouro de fogos de artificio,  indo de 10 até 0,  com uma pausa de 1 segundo'''

from time import sleep

for i in range(10,-1,-1):
    print(i)
    sleep(1)
print('\nPA PA PO PO')
