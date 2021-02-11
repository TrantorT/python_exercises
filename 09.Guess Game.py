

import random

numero = random.randint(1,10)
bingo = False
count = 0

while bingo == False:
    count+=1
    escolha = int(input("Guess a number between 1-10: "))
    if (escolha>numero):
        print("Number too high!")
    elif (escolha<numero):
        print("Number too low!")
    else:
        print("BINGO!!!")
        bingo = True

print(f"You got it in {count} attempts!")
