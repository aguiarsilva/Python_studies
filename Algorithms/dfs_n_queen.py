def is_valid(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - 1 == col - row or \
           board[i] + 1 == col + row:
               return False
    return True

def dfs(row, n, board, solutions):
    if row == n:
        solutions.append(board.copy())
        return
    for col in range(n):
        if is_valid(board, row, col):
            board[row] = col
            dfs(row + 1, n, board, solutions)
            board[row] = -1

def dfs_n_queen(n: int):
    if n < 1:
        return []

    solutions = []
    board = [-1] * n
    dfs(0, n, board, solutions)
    return solutions
