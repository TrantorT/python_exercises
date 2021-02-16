count = 0
numero = int(input("Pick a number! "))
i=1

#a prime number is only divisible by 1 and itself
while i <= numero:
    if numero % i == 0 :
        print(f"{i} is a Divisor of {numero}")
        i+=1
        count+=1
    else:
        i+=1


if count == 2:
    print(f"Number {numero} is a Prime!")
else:
    print(f"Number {numero} is NOT a Prime!")

            


