#Letra B
nume = 2
deno=500
soma=0.0

n=int(input('Num. termos '))
while n<1 or n>50: #porque quando atingir o 50 o denominador é igual a 0
    n=int(input('Inválido. Num. termos positivos'))

for i in range (1, n+1): # tem que ser n+1 pois se não vai faltar 1, pois começa no 1
    soma=soma + nume/deno
    deno = deno - 10
    if nume==2:
        nume = -5
    else:
        nume = 2

print('Resultado', soma)