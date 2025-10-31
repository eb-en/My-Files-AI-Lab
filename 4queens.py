print("4 Queens problem")


def isSafe(board, row, col):
    for i in range(row):
        if board[i] == col:
            return False
        elif abs(board[i] - col) == abs(i - row):
            return False
    return True


def backtrack(board, row, n, sols):
    if row == n:
        sols.append(board[:])
        return

    for col in range(n):
        if isSafe(board, row, col):
            board[row] = col
            backtrack(board, row + 1, n, sols)
            board[row] = -1


def solve(n):
    board = [-1] * n
    sols = []
    backtrack(board, 0, n, sols)
    return sols


solution = solve(4)

for sol in solution:
    print("Current Solution: ", sol)
    for i in range(len(sol)):
        print("|", end="")
        for j in range(len(sol)):
            if sol[i] == j:
                print("Q", end="|")
            else:
                print(" ", end="|")
        print()
