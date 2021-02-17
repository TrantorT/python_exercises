import random





def rnumber(user_num):
    numb=''
    for n in range(0,int(user_num)):
        numb+=str(random.randint(0,9))
    print(numb)



if __name__=="__main__":
    user_num = input("How many numbers for the Cow & Bulls game? : ")

    rnumber(user_num)

    print("OK The number has been generated \n")

    t = input("Guess the number:  \n")