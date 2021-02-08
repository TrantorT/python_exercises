#https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

name = input("Hello, what is your name? ")
age = input("and your age?")

idade = int(age)

x = (100 - idade) + 2021

print(f"Hello {name}, you will turn 100 years old in {x}")
