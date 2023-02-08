n1= int(input('N1'))
n2 = int(input('N2'))
n3 = int(input('N3'))

if n1>n2:
    if n1<n3:
        menor=n1
    else:
        menor = n3
else:
    if n2<n3:
        menor = n2
    else:
        menor = n3
print('Resultado',menor)

