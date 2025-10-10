import math

board = [" " for _ in range(9)]


def printBoard():
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(board[i * 3 + j], end="|")
        print()


def checkWinner(board):
    wins = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]

    for c in wins:
        if board[c[0]] == board[c[1]] == board[c[2]] != " ":
            return board[c[0]]

    if " " not in board:
        return "Tie"

    return None


def availableMoves(board):
    moves = []
    for i, j in enumerate(board):
        moves.append(i) if j == " " else None
    return moves


def minimax(board, is_maximizing):
    result = checkWinner(board)
    if result == "X":
        return -1
    elif result == "O":
        return 1
    elif result == "Tie":
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in availableMoves(board):
            board[move] = "O"
            score = minimax(board, False)
            board[move] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in availableMoves(board):
            board[move] = "X"
            score = minimax(board, True)
            board[move] = " "
            best_score = min(score, best_score)
        return best_score


def bestMove():
    best_score = -math.inf
    move_chosen = None
    for move in availableMoves(board):
        board[move] = "O"
        score = minimax(board, False)
        board[move] = " "
        if score > best_score:
            best_score = score
            move_chosen = move
    return move_chosen


def printWinner(result):
    if result == "X":
        return "You are the winner"
    elif result == "O":
        return "Bot is the winner"
    else:
        return "Tie"


print("Tic Tac Toe")
printBoard()


while True:
    move = int(input("Enter your move: "))

    if move >= 9 or board[move] != " ":
        print("Invalid Move!! Try Again")
        continue
    board[move] = "X"

    if checkWinner(board):
        print()
        printBoard()
        print(f"Game Over! {printWinner(checkWinner(board))}")
        break

    bot_move = bestMove()
    board[bot_move] = "O"
    printBoard()
    print("Bot made it's move")

    if checkWinner(board):
        print()
        printBoard()
        print(f"Game Over! {printWinner(checkWinner(board))}")
        break
