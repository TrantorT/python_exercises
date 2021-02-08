#https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

msg = input("Qual a palavra?")
rev = msg[::-1]
print(rev)

if msg == rev:
    print("Its a Palindrome!!")
else:
    print("Its NOT a Palindrome")

# abc
# cba