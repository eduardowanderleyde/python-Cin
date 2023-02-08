## Retornar menor valor até a leitura do zero
mylist = []
soma = 0
num=0
while num>=0:
    num = int(input("Digite o número: "))
    mylist.append(num)    
    for n in mylist:
        soma+=n
        n=n+1
result = soma-(n-1) / len(mylist)-1
print(result)