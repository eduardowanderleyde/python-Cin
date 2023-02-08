num1 = int(input("digite número o menor número em Fahrenheit:"))
num2 = int(input("digite número o maior número em Fahrenheit:"))

value = 0
print("Valores em Celsius", "|" ,"Valores em Fahrenheit")
for i in range(num1,num2):
    c=((i-32)*5)/9
    value += 1
    print(int(c), "|", i)