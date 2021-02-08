n = int(input("Escolha um numero"))
count = 0
i = 1
while i <= n:
    if n % i == 0:
        count+=1
        i+=1
    elif n % i ==1:
        count+=1
    else:
        i+=1
    


print(count)

            


