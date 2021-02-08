#https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

import random

size = int(input("How big you want the list to be?: "))

#sequential list
#list1 = list(range(0,size,1))
#print(list1)

#random list
listrand =  random.sample(range(1, 100), size)
print(listrand)

list2 =[]

for l in listrand:
    if l <6:
        #print(l)
        list2.append(l)


print(f"This list only contains numbers equal or smaller than 5: {list2}")
    