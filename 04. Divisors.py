#https://www.practicepython.org/exercise/2014/02/26/04-divisors.html

numero = int(input("Pick a number! "))

i=1
while i < numero:
    if numero % i == 0 :
        print(f"{i} is a Divisor of {numero}")
        i+=1
    else:
        i+=1

