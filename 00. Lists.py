import random

#lists
lista = [1,2,'tres','quatro',5]
print(lista)

#add to list
lista.append('seis')
print(lista)

#pop - takes element based on index
lista.pop(-1)
print(lista)

#remove - takes element based on value
lista.remove('quatro')
print(lista)

#iterate
for i in lista:
    print(i)

#generate random list
lista2 = []
for i in range(0,50):
    n = random.randint(1,30)
    lista2.append(n)
print(lista2)

