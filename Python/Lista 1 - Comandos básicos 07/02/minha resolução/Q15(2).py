#sem usar lista

num=int(input('Num. termo 1 '))

if num>1:
    for i in range(2,num):
        if num % i ==0:
            print(num, "não é primo")
        else:
            print(num, 'é primo')