def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
        grid (list[list[int]]): A 2D list representing the island where 0 represents water and 1 represents land.

    Returns:
        int: The perimeter of the island.

    """
    def count_edges(matrix):
        """Counts the number of edges along horizontal direction."""
        count = 0
        for row in matrix:
            row = [0] + row + [0]
            for i in range(1, len(row)):
                count += row[i] != row[i - 1]
        return count

    # Transpose the grid to count edges along vertical direction
    tgrid = [[] for _ in range(len(grid[0]))]
    for row in grid:
        for i, item in enumerate(row):
            tgrid[i].append(item)

    # Sum the edges counted in horizontal and vertical directions
    return count_edges(grid) + count_edges(tgrid)
