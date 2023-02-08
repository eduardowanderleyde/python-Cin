# somar os inteiros pares entre 50 e 100
num1=50
soma=0


while num1<=100:
    if num1%2==0:
        soma = soma+num1
    num1+=1
print(soma)
