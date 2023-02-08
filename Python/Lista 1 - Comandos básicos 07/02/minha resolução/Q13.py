num = int(input("Digitar 1 número: "))
num2 = int(input("Digitar 2 número: "))
mdclist = []
for i in range(1,max(num, num2)):
    if num % i == 0 and num2 % i == 0:
        mdclist.append(i)
print(max(mdclist))