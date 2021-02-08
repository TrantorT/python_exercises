# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
# and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.

import random

size = int(input("What size of list you want?:\n"))
lista1 = []
for i in range(0,size):
    n = random.randint(1,30)
    lista1.append(n)
print(f"This is the original List with {size} elements:\n {lista1}")

newlist = []
newlist.append(lista1[0])
newlist.append(lista1[-1])
print(f"This is the new list with 1st and last element:\n {newlist}")
