#https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

number = int(input("Please pick a number! "))

if number % 2 == 0:
    if number % 4 == 0:
        print("You picked an EVEN number that is also a multiple of 4!!")
    else:
        print("You picked an EVEN number!")
else:
    print("You picked an ODD number!")