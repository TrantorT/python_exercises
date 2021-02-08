

import random

numero = random.randint(1,9)
bingo = False
count = 0

while bingo == False:
    count+=1
    escolha = int(input("Adivinha um numero entre 1-9: "))
    if (escolha>numero):
        print("Numero demasiado alto")
    elif (escolha<numero):
        print("Numero demasiado baixo")
    else:
        print("BINGO!!!")
        bingo = True

print(f"Acertaste em {count} tentativas!")
