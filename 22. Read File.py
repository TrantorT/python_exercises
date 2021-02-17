#count how many names there are in file names.txt
# 

#lista de nomes
names = []
unique = {}



with open('names.txt', 'r') as open_file:
    for line in open_file.readlines():
        names.append(line.rstrip())
    for i in names:
        if i in unique:
            unique[i] +=1
        else:
            unique[i]=1

print(unique)



#count categories
cat = []
uniquecat = {}

with open('directories.txt', 'r') as open_file:
    for line in open_file.readlines():
        cat.append(line.rstrip().split('/')[2])
    for i in cat:
        if i in uniquecat:
            uniquecat[i] +=1
        else:
            uniquecat[i]=1

print(uniquecat)



    
   