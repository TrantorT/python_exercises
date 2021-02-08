#https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

name = input("Hello, what is your name?\n")
age = input("and your age?\n")

idade = int(age)

x = (100 - idade) + 2021

if idade > 10 and idade < 90:
    print(f"Hello {name}, you will turn 100 years old in {x}")
else:
    print(f"Hello {name}, I don't really believe your age, but according to my calculations you would turn 100 years old in {x}")
