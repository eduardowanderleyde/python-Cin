num= int(input("numero:"))
def fatorial (num):
    f=1
    
    for i in range (2,num+1):
        f=f*i
    
fat = fatorial (num) 
print(fat)