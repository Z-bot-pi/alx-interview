#!/usr/bin/python3
'''
Module that solves the N Queens puzzle
'''
from sys import argv, exit

if __name__ == "__main__":
    if len(argv) != 2:
        print('Usage: nqueens N')
        exit(1)
    
    try:
        n = int(argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)
    
    if n < 4:
        print('N must be at least 4')
        exit(1)

    # Solution list to store each configuration
    solution = []

    def solve_queens(row, n, solution):
        # Base case: if row == n, we've placed all queens successfully
        if row == n:
            print(solution)
        else:
            # Try to place a queen in every column in the current row
            for col in range(n):
                placement = [row, col]
                if valid_placement(solution, placement):
                    solution.append(placement)  # Place queen
                    solve_queens(row + 1, n, solution)  # Recur to place the next queen
                    solution.pop()  # Backtrack and remove the queen

    def valid_placement(solution, placement):
        # Check if current placement is valid based on queens already placed
        for queen in solution:
            # Same column check
            if queen[1] == placement[1]:
                return False
            # Major diagonal check
            if (queen[0] + queen[1]) == (placement[0] + placement[1]):
                return False
            # Minor diagonal check
            if (queen[0] - queen[1]) == (placement[0] - placement[1]):
                return False
        return True

    # Start solving from row 0
    solve_queens(0, n, solution)

