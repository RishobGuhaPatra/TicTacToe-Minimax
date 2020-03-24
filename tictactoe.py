""" Tic tac toe with AI
    CPU is O
    User is X       """

from sys import(stdout)
import math
import random

#create board to store x and o with variable size
size = int(input("enter size: "))
#board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
board = []

for i in range(size):
    row = [' ' for i in range(size)]
    board.append(row)

def insert(letter, pos):
    """ adds the specified letter (x or o) to the desired position """
    row = math.floor(pos / size)
    col = math.floor(pos % size)
    board[row][col] = letter

def spaceFree(pos):
    """ used to check if the space we want to insert at is avail.
        returns true or false """
    row = math.floor(pos/size)
    col = math.floor(pos%size)
    return board[row][col] == ' '

def printBoard(board):
    """ prints the board in a readable format"""
    for row in board:
        for ele in row:
            if ele == ' ':
                stdout.write("|   |")
            else:
                stdout.write('| ' + ele + ' |')
        print('\n')


def isWinner(board, letter):
    """ checks if letter has won based on the current board
        returns 0 if letter has not won """
    # if row is all one letter
    for row in board:
        if set(row) == set(letter):
            return True
    # if col is all one letter
    for col in zip(*board):
        if set(col) == set(letter):
            return True
    # if either diag is all one letter
    lrDiag = []         # keep track of elements in the LR diagonal
    i = 0
    rlDiag = []         # keep track of elements in the RL diagonal
    j = size - 1
    for ele in board:
        lrDiag.append(ele[i])
        rlDiag.append(ele[j])
        i = i + 1
        j = j - 1
    if set(lrDiag) == set(letter) or set(rlDiag) == set(letter):
        return True

    return False

def playerMove():
    run = True
    while run:
        stdout.write('Select a position to place an X (0 - {}'.format(size**2 - 1))
        move = int(input('): '))
        # input validation
        try:
            move = int(move)
            if 0 <= move < size**2:
                if spaceFree(move):
                    run = False
                    insert('X', move)
                else:
                    print("Sorry this space is occupied.")
            else:
                print("Please input a number with the range")
        except:
            print("Please type a number.")

def cpuMove():
    run = True
    if isFull(board):
        return -1
    while run:
        move = random.randint(0, (size**2)-1)
        if spaceFree(move):
            run = False
            insert('O', move)
    return move

def selectRand():
    pass

def isFull(board):
    """ return true or false if the board is full """
    for row in board:
        if row.count(' ') > 0:
            return False
    else:
        return True

def main():
    print("INITIAL BOARD:\n")
    printBoard(board)
    # run the game
    while not isFull(board):
        if not(isWinner(board, 'O')):   # check if CPU has won
            playerMove()
            printBoard(board)
        else:
            print("Sorry, O is winner!")
            break
        if not(isWinner(board, 'X')):   # check if player has won
            move = cpuMove()
            if move == -1:
                print("Tie game!")
                break
            else:
                insert('O', move)
                print('Computer placed an O in position ', move)
                printBoard(board)
        else:
            print("X is the winner. Good job!")
            break

    if isFull(board):
        print("Tie game!")
main()