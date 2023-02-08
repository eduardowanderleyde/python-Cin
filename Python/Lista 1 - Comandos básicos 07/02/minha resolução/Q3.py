# Ler 3 numeros e imprimir o menor deles


num1= int(input('Numero 1:'))
num2= int(input('Numero 2:'))
num3= int(input('Numero 3:'))

maior=num1
#achando o maior número
if num2>maior:
    maior = num2
if num3>maior:
    maior = num3
print('Maior',maior)


#achando o menor número
menor = num1
if num2<menor:
    menor = num2
if num3<menor:
    menor = num3
print('Menor',menor)
