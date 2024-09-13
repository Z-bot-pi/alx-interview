#!/usr/bin/python3
"""N queens
"""

import sys


def print_solution(board):
    """print board"""
    solution = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)


def safe(board, row, col, n):
    """Function to check if a queen can be placed on board"""
    for c in range(col):
        if board[row][c] == 1:
            return False

    for r, c in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[r][c] == 1:
            return False

    for r, c in zip(range(row, n, 1),
                    range(col, -1, -1)):
        if board[r][c] == 1:
            return False

    return True


def solution(board, col, n):
    if col == n:
        print_solution(board)
        return True

    c = False
    for i in range(n):
        if safe(board, i, col, n):
            board[i][col] = 1
            c = solution(board, col + 1, n) or c
            board[i][col] = 0
    return c


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        exit(1)

    try:
        n = int(sys.argv[1])

    except Exception:
        print('N must be a number')
        exit(1)

    if n < 4:
        print('N must be at least 4')
        exit(1)

    board = [[0 for i in range(n)] for j in range(n)]
    solution(board, 0, n)