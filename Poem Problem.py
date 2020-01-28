file = open("Poemtext.txt","r")
exception = ("i","I")
count = 0

for x in file:
    #print(x)
    for y in x:
        #print(y)
        if y in exception:
            count = count + 1
print(str(count) + " letter I's were counted")

file.close()