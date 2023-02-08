num=int(input('Num. termo 1 '))
num2=int(input('Num. termo 2'))

while num<=0: #validar se é positivo
    num=int(input('Inválido os termos tem que ser positivos. Digite novamente n1:'))

while num2<=0:
    num2=int(input('Inválido os termos tem que ser positivos. Digite novamente n2:'))

if num>num2: #validar maior numero já que são apenas 2
    maior= num
else:
    maior= num2

for i in range (maior):
    aux=num*i
    if(aux % num2)==0:
        mmc = aux

print(mmc)