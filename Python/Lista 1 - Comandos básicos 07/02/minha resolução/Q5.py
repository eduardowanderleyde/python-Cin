# calcular o fatorial de um número lido

n=int(input('Numero 1:'))
fat=1

for i in range(1,n+1):
    fat=fat*i
print(f'o valor de fat é',fat)
