soma = 0.0
qtd = 0
num= float(input('Numero'))

while num>=0:
    soma=soma+num
    qtd = qtd+1
    num = float(input('Numero'))

if qtd>0:
    soma = soma/qtd
    print('Resultado', soma)
else:
    print('nenhum numero valido digitado')