#!/usr/bin/python3

def island_perimeter(grid):
    """Computes the perimeter of an island with no lakes."""
    perimeter = 0
    if not isinstance(grid, list):  # Use isinstance for type checking
        return 0
    n = len(grid)
    m = len(grid[0]) if grid else 0  # Avoid index out of range
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                continue
            edges = (
                i == 0 or grid[i - 1][j] == 0,  # Simplify conditions
                j == m - 1 or grid[i][j + 1] == 0,
                i == n - 1 or grid[i + 1][j] == 0,
                j == 0 or grid[i][j - 1] == 0,
            )
            perimeter += sum(edges)
    return perimeter
