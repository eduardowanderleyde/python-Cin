l1 = [1,2,3,4,5,6,7,8,9]
ex1=[variavel for variavel in l1]

ex2= [v*2 for v in l1]
print(ex2)
ex3= [(v,v2) for v in l1 for v2 in range(3)]
print(ex3)

l2=['Luiz','Mauro','Maria']
ex4=[v.replace('a','@') for v in l2]
print(ex4)

tupla = (('chave','valor'),('chave2','valor2'),)
ex5=[(y,x) for x,y in tupla]
ex5=dict(ex5)
print(ex5('valor2'))