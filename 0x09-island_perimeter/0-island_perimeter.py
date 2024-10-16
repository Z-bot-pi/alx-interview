#!/usr/bin/python3
"""
Module to define island perimeter calculation.
"""

def island_perimeter(grid):
    """
    Function to calculate the perimeter of an island in a grid.
    
    Parameters:
    grid (list of list of int): 2D list representing the grid, where 0 is water and 1 is land.
    
    Returns:
    int: Perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4  # Add 4 for each land cell

                # Check the neighboring cells (up and left) and reduce the perimeter accordingly
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2  # Subtract 2 for the shared edge with the upper cell
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2  # Subtract 2 for the shared edge with the left cell

    return perimeter
