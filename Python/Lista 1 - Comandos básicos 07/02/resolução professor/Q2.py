n1= int(input('N1'))
n2 = int(input('N2'))

while n2==0:
    n2 = int(input('Inválido, digite novamente N2'))
    
resto =n1%n2
if resto== 0:

    res = n1
else:
    res=resto**2

print('Resultado', res)



