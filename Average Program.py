high = 0 # variable for the higest num
low = 0 # variable for the lowest num
duration = 0 # variable for the amount of times the loop will run for
data = 0 # input data

duration = int(input("How many numbers do you want to enter? "))
#grabs the user the input and stores it into duration

if duration == 0:
    print("ThANks FoR USiNg ThIS pROgrAM")
    exit()
# kills the program if the user does not want to enter a number

data = int(input("Please input a number: "))
high = data
low = data
# grabs the first input and store it into data, then it is stored into high and low

for i in range (duration - 1):
    # loops for duration - 1 because it has already asked for a number
    data = int(input("Please input the next number: "))
    # grabs the user input
    if data > high:
        high = data
        # if the input data is higher than the current number in high, then the it's stored into high
    elif data < low:
        low = data
        # else if the input data is lower than the current number in low, then the it's stored into low


print("The average of the numbers is: " + str( (high + low) / 2))
# prints the average, *must be converted to type string*
