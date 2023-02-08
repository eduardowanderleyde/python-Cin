
numeros = [64,532,86,5,44,500,875,432,0,5234,764,6,234,53,876]
for i in range(len(numeros)):
    if numeros[i] == 0:
        minimo = i-1
print(min(numeros[:minimo]))
