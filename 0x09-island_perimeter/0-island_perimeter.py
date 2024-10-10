# 0-island_perimeter.py

def island_perimeter(grid):
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Add 4 for the current land cell
                perimeter += 4

                # Check if the cell above is also land
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2  # Remove 2 for the shared edge with the cell above

                # Check if the cell to the left is also land
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2  # Remove 2 for the shared edge with the cell to the left

    return perimeter
