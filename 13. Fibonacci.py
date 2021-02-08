#0, 1, 1, 2, 3, 5, 8, 13, 21, 34

def fibonacci(size):
    
    fibo = []

    for i in range(size):
        #print(i)
        if i > 0:
            fibo.append(fibo[i]+fibo[i-1])
        else:
            fibo.append(0)
            fibo.append(1)
    

    return fibo



size = int(input("How many numbers for the Fibonacci sequence?\n"))
print(f"This is the Fibonacci sequence with {size} numbers: {fibonacci(size)}")


