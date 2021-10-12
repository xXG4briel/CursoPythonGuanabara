# leia o primeiro termo e a razao de uma progressão aritmética no final, mostre os 10 primeiros termos dessa progressão

text='-='*25
pa='Progressão Aritmética'
print(f'{text}\n{pa: ^50}\n{text}')

termo=int(input('Digite o primeiro termo: ')) # onde se quer começar
razão=int(input('Digite a razão: ')) # de quanto em quanto se deve pular

décimo = termo +(10* razão)

print(décimo)

for i in range(termo,décimo,razão):
    print(f'{i}',end=' → ')
print(' Acabou ')
    
