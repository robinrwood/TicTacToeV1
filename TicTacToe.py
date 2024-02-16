import random


def main():
    gameBoard = [["0", "1", "2"],
                 ["3", "4", "5"],
                 ["6", "7", "8"]]
    compTurn = intro(gameBoard)
    isFull(gameBoard, compTurn)


def intro(board):
    print("Welcome to Robin's Tic Tac Toe (v1)!")
    print()
    print("This tic tac toe game is played against the computer "
          "(represented by O) and a human (represented by X). "
          "Who goes first will be randomly selected.")
    printBoard(board)

    turn = random.randrange(0, 2)
    if turn == 0:
        print("Computer goes first.")
        return True
    else:
        print("Human goes first")
        return False



def computerPlay(board):
    # empty spot
    empty = False

    # computer plays
    row = random.randrange(0, 3)
    col = random.randrange(0, 3)

    # check if spot is empty
    while not empty:
        if board[row][col] != "X" and board[row][col] != "O":
            board[row][col] = "O"  # add play to gameBoard
            empty = True
        else:
            row = random.randrange(0, 3)
            col = random.randrange(0, 3)



def humanPlay(board):
    printBoard(board)

    # human plays
    play = input("Please pick a position between 0 and 8 that is empty: ")

    # check if play is valid
    while not isValid(board, int(play)):
        play = input("Please pick a position between 0 and 8 that is empty: ")

    # play added to game board
    for row in range(0, 3):
        for col in range(0, 3):
            if board[row][col] == play:
                board[row][col] = "X"


def printBoard(board):
    print("---+---+---")
    print(board[0][0], " |", board[0][1], " |", board[0][2])
    print(board[1][0], " |", board[1][1], " |", board[1][2])
    print(board[2][0], " |", board[2][1], " |", board[2][2])
    print("---+---+---")
    print()
    return board


def isValid(board, play):
    # check range
    if play > 8 or play < 0:
        print("Your input is out of range!")
        return False
    else:
        # check if position is already taken
        for row in range(0, 3):
            for col in range(0, 3):
                if board[row][col] == str(play):
                    return True
        print("That position is already taken.")
        return False


def isWinner(board):
    winner = False

    # check rows
    for row in range(0, 3):
        if board[row][0] == board[row][1] == board[row][2] == "X":
            winner = True
            print("Human, you won!")

        elif board[row][0] == board[row][1] == board[row][2] == "O":
            winner = True
            print("Computer won!")

    # check columns
    for col in range(0, 3):
        if board[0][col] == board[1][col] == board[2][col] == "X":
            winner = True
            print("Human, you won!")
        elif board[0][col] == board[1][col] == board[2][col] == "O":
            winner = True
            print("Computer won!")

    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] == "X":
        winner = True
        print("Human, you won!")

    elif board[0][0] == board[1][1] == board[2][2] == "O":
        winner = True
        print("Computer won!")

    elif board[0][2] == board[1][1] == board[2][0] == "X":
        winner = True
        print("Human, you won!")

    elif board[0][2] == board[1][1] == board[2][0] == "O":
        winner = True
        print("Computer won!")

    if winner:
        printBoard(board)

    return winner


def isFull(board, turn):
    count = 0
    winner = False

    while count < 10 and winner == False:
        # play
        if turn:
            computerPlay(board)
        else:
            humanPlay(board)
        turn = not turn
        count += 1

        # check for winner
        winner = isWinner(board)  # change depending on what is being returned

        if count == 9:
            print("The board is full. The game is over.")
            if not winner:
                print("It's a tie.")
            if winner and turn:
                print("Human wins!")
            if winner and not turn:
                print("Computer wins!")


main()
