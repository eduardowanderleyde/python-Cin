num1 = int(input("digite o número de termos:"))
count_imp = 0
count_par = 0
for i in range(1,num1):
        if i % 2 != 0:
            count_imp += 1
        elif i % 2 == 0:
            count_par += 1
if num1 % 2 != 0:
    N = count_imp*5 + count_par*1 - 1
else:
    N = count_imp*5 + count_par*1 - 5
print(N)