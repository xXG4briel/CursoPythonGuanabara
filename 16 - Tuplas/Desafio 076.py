produtos = ('Notebook',2500,'Celular',900,'Impressora',750,'Alexa',300,'Borracha',1,'LÁapis',2,'Computador',3800)

print('{}\n{: ^50}\n{}'.format('-'*50,'Lojão nicão','-'*50))
var=35

for i in range(len(produtos)):
    if i%2 ==0 :
        print(produtos[i],'.'*(var-len(produtos[i])) , end='')
        print(f' R$ {produtos[i+1]:7.2f}')
    
