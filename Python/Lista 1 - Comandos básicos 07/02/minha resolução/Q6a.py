#Calcular o valor de S com N termos, onde N é informado pelo usuário e:
# a.S=1+3/2+5/3+7/4...


h = 3
n = 2
h_lista = []
n_lista = []
contador=int(input("Qual o N:"))
print("H = 1 +", end = "")
while n <= contador -1:
    print(" ",h, "/", n, " + ", end="")
    h_lista.append(h)
    n_lista.append(n)
    h +=2
    n += 1

print(h, "/", n, " => ", sum(h_lista), "/", sum(n_lista), " => ", sum(h_lista) / sum(n_lista)) 