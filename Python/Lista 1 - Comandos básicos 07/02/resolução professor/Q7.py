soma=0
n1=int(input ('N1'))
n2=int(input ('N2'))

if n2<n1:
    n1,n2=n2,n1
    for i in range (n1,n2+1,2):
        soma = soma+i
    print('Resultado', soma, 'para', n1'e',n2)