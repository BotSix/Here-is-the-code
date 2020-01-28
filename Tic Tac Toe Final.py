# Primitive Tic-Tac-Toe Game in Python ICS2O HSC
# This game uses a 2d board to store a 3x3 grid of values
# these values are first positions 1-9 which are then replaced
# by the two human players of the game called tic-tac-toe
# A player wins by having three x's or o's in a row, column or diagonal
# Author: Mr. Reid & Chen Qing
# Date: 11/21/2019

# Global Variables: - setting up the board [row][col]
import sys

board = [[0 for x in range(3)] for y in range(3)]

player = ' x '  # or set to ' o ' for player o turn

# populating the rows and columns with the corresponding values

board[0][0] = ' 1 '
board[0][1] = ' 2 '
board[0][2] = ' 3 '
board[1][0] = ' 4 '
board[1][1] = ' 5 '
board[1][2] = ' 6 '
board[2][0] = ' 7 '
board[2][1] = ' 8 '
board[2][2] = ' 9 '

# display the tic tac toe board
def display():
    for r in range(3):
        
        print(" ",end="")
        for c in range(3):
            print(board[r][c], end="")
            if c < 2:
                print("|",end="")
        print()
        if(r < 2):
            print(" ---|---|---")
# end of display

# gets the user input and decides if the move is valid or not
def turn(player):
    
    data = input("please enter 1-9 to make your move (0 to quit): ")
    while data.isdecimal() == False:
        data = input("Error: enter 1-9 to make your move (0 to quit): ")
    # protects the input

    loc = int(data)            # the location of the move
    r = int((loc - 1) / 3)
    c = int((loc - 1) % 3)

    if board[r][c] == ' x ' or board[r][c] == ' o ':
        loc = -1
    else:
        board[r][c] = player     

    return loc                  # returns the value in loc which allows the program to check for win, tie, and invalid moves

""" This function checks if there is a row of 3(x's or o's) in any possible combination to check if 
either player has won. Looks to see if each row, column, or diagnal row has the same values inside it."""

def win(): 
    for r in range(3):
            if board[r][0] == board [r][1] and board[r][1] == board[r][2] and board[r][0] == board [r][2]:
                return True
    for c in range(3):
            if board[0][c] == board [1][c] and board[1][c] == board[2][c] and board[0][c] == board [2][c]:
                return True
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == board[2][2]:
        return True
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] == board[2][0]:
        return True

""" This function checks if all the spaces are filled up. It goes through each board to adds 1 to checkerVal for each
occupied """

def spaceChecker(): 
    checkerVal = 0
    for r in range (3):
        for c in range(3):
            if board[r][c] == ' x ' or board[r][c] == ' o ':
                checkerVal += 1
    return checkerVal

# --------------- The Main Program ---------------------

print("Welcome to a game of tic-tac-toe")
print("--------------------------------")
print()
print("to play enter a position labled 1 to 9")
print("player 1 will be x and player 2 will be o")
print()

display()

def main():
    looper = False
    global player
    while looper == False: # master loop
        dataIn = turn(player) # stores player input into a variable
        while dataIn >= 1 and dataIn <= 9: # main program loop, this will only run when the input from the player is in the range of the board(1-9)
            display()
            if player == ' x ':     # switch player between moves
                player = ' o '
            else:
                player = ' x ' 
            dataIn = turn(player) # stores player input into a variable
            if win() == True: # if none of the spaces are filled up but a player has won
                print("You won")
                looper = True # breaks master loop
                break # breaks main program loop
            elif spaceChecker() == 9: # if no one's won but all the space are filled up, it is a tie
                print("Tie")
                looper = True # breaks the master loop
                break # breaks the main program loop
            
        if dataIn == 0: # if the input from the user is not 0, the program checks if it is an invalid move(return of -1)
            sys.exit()
        if dataIn == -1:# if there is an invalid move, the program prints an error message
            print("Invalid Move")

while True: # the main program is put into a function, this loop allows the users to play the game over and over
    board[0][0] = ' 1 '
    board[0][1] = ' 2 '
    board[0][2] = ' 3 '
    board[1][0] = ' 4 '
    board[1][1] = ' 5 '
    board[1][2] = ' 6 '
    board[2][0] = ' 7 '
    board[2][1] = ' 8 '
    board[2][2] = ' 9 '
    main() # main program
    display() # displays grid after the game is over
    Input = input("Do you want to play again? (Y/N): ")
    if Input == "Y": #
        print() # place holder since python does not allow empty if statements
    elif Input == "N":
        break # breaks the main loop
    else:
        print() # place holder since python does not allow empty if statements
        
print("Thank you for playing!")