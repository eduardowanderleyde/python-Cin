lista = []
num=0
while num !=99:
    num = int(input())
    lista.append(num)

lista.sort(reverse=True)

lista.pop(0)  

print(lista[1])