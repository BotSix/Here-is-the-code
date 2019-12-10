"""
This program is a simple enryption and decryption program. It puts all the characters in the alphabet into a list which assigns each
character with a numerical value. It asks for user input and matches the characters from the user input with the alphabet and assigns 
the characters with a numerical value(the index). The key is either added or subtrated from the index depending if it's encrypting or
decrypting and returns the values in the encrypted index location. It combines those values into a string and returns it to the user.
"""

global shift # encryption or decryption key
global Alpha # array containing the characters in the alphabet
global inputList # array containing the characters of the inputted string
global indexLoc # array containing the indexes of the characters
global outputList # list of the characters in encrypted or decrypted message
global outputString # string of the decrypted or decrypted message

Alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ ") # splits up each character in the alphabet and a space into a list
indexLoc = [] # empty list for the index of the letter once encrypted or decrypted
inputList = [] # empty list of each character from the input
outputList = [] # empty list of each character from the output
outputString = "" # string of the output

def encrypt(data, shift): # encryption function
    inputList = list(data) # splits the characters from the input data into a list
    for i in range(len(inputList)): # starts a for loop that loops for how ever many characters were inputted by the user
        if inputList[i] == ' ': # checks if there is a space from the input, if so, the index of the space from Alpha will be saved into indexLoc
            indexLoc.append(Alpha.index(' '))
        else: 
            if (int(Alpha.index(inputList[i])) + int(shift)) > 25: # checks if the shift will be greater than the mac character index
                indexLoc.append((int(Alpha.index(inputList[i])) + int(shift)) % 26) 
                # if so, adds the shift to the character index and takes the reminder from dividing by 26
                #then appends it to the indexLoc
            else:
                indexLoc.append(Alpha.index(inputList[i]) + int(shift))
                # if the shift does not exceed the max character index, then the shifted value is appended to indexLoc

        outputList.append(Alpha[indexLoc[i]])
    print("Your translated text is: " + outputString.join(outputList)) # outputs the encrypted characters joined as a single string
        
def decrypt(data, shift): # decryption function
    inputList = list(data) # splits the characters from the input data into a list
    for i in range(len(inputList)): # starts a for loop that loops for how ever many characters were inputted by the user
        if inputList[i] == ' ': # checks if there is a space from the input, if so, the index of the space from Alpha will be saved into indexLoc 
            indexLoc.append(Alpha.index(' '))
        else:
            if (int(Alpha.index(inputList[i]) - int(shift))) < 0:
                indexLoc.append(25 - abs(int(Alpha.index(inputList[i]) - int(shift))) % 26)
            else: indexLoc.append(Alpha.index(inputList[i]) - int(shift))
        outputList.append(Alpha[indexLoc[i]])
    print("Your translated text is: " + outputString.join(outputList))

data = input("Do you wish to encrypt or decrypt a message? ")
if data == "encrypt":
    data = input("Please enter the message (A-Z only): ")
    data = data.upper()
    shift = input("Please enter the key number: ")
    encrypt(data,shift)
elif data == "decrypt":
    data = input("Please enter the message (A-Z only): ")
    data = data.upper()
    shift = input("Please enter the key number: ")
    while shift.isnumeric() == False:
        print("Sorry, integers only")
        shift = input("Please enter the key number: ")
    decrypt(data,shift)
else:
    print("Error please enter encrypt or decrypt")




