numeros=[]
maiores=[]
num=0
while num!=99:
    num=int(input())
    numeros=numeros+[num]

numeros=numeros[:-1] 
def maior_numero(numeros :list):
    if len(numeros) >=2:
        maior=numeros[0]
        indice=0
        for i in range(len(numeros)):
            if numeros[i]>maior:
                maior=numeros[i]
                indice=i
        return indice
    elif len(numeros)==1:
        return 0  
    else:
        return '' 
    
while len(numeros)!=0:
    indice=maior_numero(numeros)
    maiores= maiores+[numeros[indice]]
    del numeros[indice]

if len(maiores)>2:
    i=0
    maior2= maiores[1]
    while maiores[i]==maiores[i+1]:
        maior2=maiores[i+2]
        i=i+1
    print("%d"%(maior2)) 
elif len(maiores)==2:
    maior2= maiores[1]
    print("%d"%(maior2))