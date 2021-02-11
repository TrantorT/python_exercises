import random

lista1 = []
for i in range(0,50):
    n = random.randint(1,30)
    lista1.append(n)
print(lista1)

#a set has no duplicates, thats the easy way
x = set(lista1)
print(x)

#another list
lista2 = []
#for i in lista1: