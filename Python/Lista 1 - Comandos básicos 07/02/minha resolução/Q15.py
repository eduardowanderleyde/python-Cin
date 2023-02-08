num=int(input('Num. termo 1 '))

while num<=0: 
    num=int(input('Inválido os termos tem que ser positivos. Digite novamente n1:'))

lista=[]
for i in range(1,num+1):
    if num%i==0:
        lista.append(num)
       
        
if len(lista)==2:
    print('é primo', num)
else:
    print('não é primo')