#!/usr/bin/python3
import sys

def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check for another queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row, col
    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_nqueens(board, row, solutions):
    """Use backtracking to place queens and record solutions."""
    n = len(board)
    if row == n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_nqueens(board, row + 1, solutions)
            board[row][col] = 0  # backtrack

def nqueens(n):
    """Solve the N queens problem and print each solution."""
    board = [[0] * n for _ in range(n)]
    solutions = []
    solve_nqueens(board, 0, solutions)
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    nqueens(N)



