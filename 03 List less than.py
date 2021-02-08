#https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

lista = [1,2,3,4,5,6,7,8,9,0,2,4,5,6,23,231,543,45,6,54,21,1,3,]

lista2 =[]

for l in lista:
    if l <6:
        print(l)
        lista2.append(l)


print(lista2)
    