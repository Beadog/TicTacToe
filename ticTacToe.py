'''
Corrie Stewart
TicTacToe
Date: 10/7/18
'''

import sys

def main():
    gameBoard = [[" ", " ", " "],
                 [" ", " ", " "],
                 [" ", " ", " "]]

    printBoard(gameBoard)

    while True:
        #
        playerXturn(gameBoard)
        printBoard(gameBoard)
        if isWin(gameBoard):
            print("Player X wins!")
            sys.exit()
        elif boardFull(gameBoard):
            print("Draw. No more plays left.")
            sys.exit()

        playerOturn(gameBoard)
        printBoard(gameBoard)
        if isWin(gameBoard):
            print("Player O wins!")
            sys.exit()
        elif boardFull(gameBoard):
            print("Draw. No more plays left.")
            sys.exit()

def printBoard(gameBoard):
    print("---------")
    print(gameBoard[0][0], "|", gameBoard[0][1], "|", gameBoard[0][2])
    print("---------")
    print(gameBoard[1][0], "|", gameBoard[1][1], "|", gameBoard[1][2])
    print("---------")
    print(gameBoard[2][0], "|", gameBoard[2][1], "|", gameBoard[2][2])
    print("---------")


def playerXturn(gameBoard):
    playerXrow = int(input("Enter a row (0, 1, or 2) for player X: "))
    playerXcolumn = int(input("Enter a column (0, 1, or 2) for player X: "))

    while gameBoard[playerXrow][playerXcolumn] == "X" or gameBoard[playerXrow][playerXcolumn] == "O":
        print("This spot is already taken. Try again:")
        playerXrow = int(input("Enter a row (0, 1, or 2) for player X: "))
        playerXcolumn = int(input("Enter a column (0, 1, or 2) for player X: "))

    gameBoard[playerXrow][playerXcolumn] = "X"

    return gameBoard

def playerOturn(gameBoard):
    playerOrow = int(input("Enter a row (0, 1, or 2) for player O: "))
    playerOcolumn = int(input("Enter a column (0, 1, or 2) for player O: "))

    while gameBoard[playerOrow][playerOcolumn] == "X" or gameBoard[playerOrow][playerOcolumn] == "O":
        print("This spot is already taken. Try again:")
        playerOrow = int(input("Enter a row (0, 1, or 2) for player O: "))
        playerOcolumn = int(input("Enter a column (0, 1, or 2) for player O: "))

    gameBoard[playerOrow][playerOcolumn] = "O"
    return gameBoard

#check for empty spaces on the board
def boardFull(gameBoard):
    for i in range(3):
        for j in range(3):
            if gameBoard[i][j] == " ":
                return False
    return True

#check for 3 in a row
def isWin(gameBoard):
    #check for row matches
    for row in range(0, 3):
        if gameBoard[row][0] == "X" and gameBoard[row][1] == "X" and gameBoard[row][2] == "X":
            return True
        if gameBoard[row][0] == "O" and gameBoard[row][1] == "O" and gameBoard[row][2] == "O":
            return True
        if gameBoard[0][row] == "X" and gameBoard[1][row] == "X" and gameBoard[2][row] == "X":
            return True
        if gameBoard[0][row] == "O" and gameBoard[1][row] == "O" and gameBoard[2][row] == "O":
            return True

    #check for diagonal matches
    if gameBoard[1][1] != " " and gameBoard[0][0] == gameBoard [1][1] and gameBoard[0][0] == gameBoard [2][2]:
        return True

    if gameBoard[1][1] != " " and gameBoard[0][2] == gameBoard [1][1] and gameBoard[0][2] == gameBoard [2][0]:
        return True

    return False

main()
