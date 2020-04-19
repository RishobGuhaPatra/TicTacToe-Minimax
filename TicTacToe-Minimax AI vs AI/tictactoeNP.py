"""
Tic-Tac-Toe Program based on a program found here:
https://www.geeksforgeeks.org/python-implementation-automatic-tic-tac-toe-game-using-random-number/
The sise of the board is arbitrary and controlled by the size variable.
The user can input moves based on the move dictionary:  { 1: (0,0), 2: (0, 1), ...}.
Players are:
1 for X (moves first)
2 for O (moves second)
Outcomes are indicated as follows:
Winner is: 1
Winner is: 2
Winner is: -1 if its a draw (cat's game)
Has nice imput checking in the make_a_move function using the try statement and exception handlling.
If the function make_a_move(board, player) is commented out and random_place(board, player) is put back in CPU will play both sides with random moves.
"""

# importing all necessary libraries
import numpy as np
import random
from time import sleep  # I commented the use of time.sleep out.   May need it for CPU play.

# Determines the size of the board (size x size)
size = 10


# Creates an empty board of zeros with dimensions size x size
def create_board():
    return (np.zeros((size, size), dtype=np.int))

# Check for empty places on board
def possibilities(board):
    l = []

    for i in range(len(board)):
        for j in range(len(board)):

            if board[i][j] == 0:
                l.append((i, j))
    return (l)


# Select a random place for the player.  The program does not use this code in the currently.
#

def random_place(board, player):
    selection = possibilities(board)
    current_loc = random.choice(selection)
    board[current_loc] = player
    return (board)


# Create a dictionary that associates the integers from 1 to size of the board with a position, (row, col), on the board.
# { 1: (0,0), 2: (0, 1), ...}

tuple_list = [(i, j) for i in range(size) for j in range(size)]
move_dict = dict(zip(range(1, size ** 2 + 1), tuple_list))


def make_a_move(board, player):
    run = True
    while run:
        move = input("Select number from 1 to {size ** 2}: ")
        try:
            move = int(move)
            if 1 <= move <= (size ** 2):
                current_loc = move_dict[move]
                if current_loc in possibilities(board):
                    run = False
                    board[current_loc] = player
                    return (board)
                else:
                    print("Sorry this space is occupied.")
            else:
                print("Please input a number within the range 1 to {size ** 2}: ")
        except:
            print("Please type a number: ")


# Checks whether the player has three
# of their marks in a horizontal row
def row_win(board, player):
    for x in range(len(board)):
        win = True

        for y in range(len(board)):
            if board[x, y] != player:
                win = False
                continue

        if win == True:
            return (win)
    return (win)


# Checks whether the player has three
# of their marks in a vertical row
def col_win(board, player):
    for x in range(len(board)):
        win = True

        for y in range(len(board)):
            if board[y][x] != player:
                win = False
                continue

        if win == True:
            return (win)
    return (win)


# Checks whether the player has three
# of their marks in a diagonal row
def diag_win(board, player):
    win = True

    for x in range(len(board)):
        if board[x, x] != player:
            win = False
    return (win)


# Evaluates whether there is
# a winner or a tie
def evaluate(board):
    winner = 0

    for player in [1, 2]:
        if (row_win(board, player) or
                col_win(board, player) or
                diag_win(board, player)):
            winner = player

    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner


# Main function to start the game
def play_game():
    board, winner, counter = create_board(), 0, 1
    print(board)
    sleep(2)

    while winner == 0:
        for player in [1, 2]:
            # board = random_place(board, player)  #  Put this line in, and comment out the next one, to have the CPU play itself with random moves randomly.
            board = make_a_move(board, player)  # Comment this line out to have CPU play itself.
            print("Board after " + str(counter) + " move")
            print(board)
            # sleep(2) # May be need for CPU play.
            counter += 1
            winner = evaluate(board)
            if winner != 0:
                break
    return (winner)


# Driver Code
print("Winner is: " + str(play_game()))