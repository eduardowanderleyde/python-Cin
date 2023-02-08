num1 = int(input("digite número mínimo:"))
num2 = int(input("digite número máximo:"))
soma = 0
i = num1
while i <= num2:
        if i%2 != 0:
            soma = soma + i
        i += 1
    
print(soma)