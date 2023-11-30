#!/usr/bin/python3
"""A module for a function"""


def island_perimeter(grid):
    """return the perimeter of the island described in grid """
    if not grid or len(grid) == 0:
        return 0
    rows = len(grid)
    columns = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == 1:
                perimeter += 4
                if column > 0 and grid[row][column - 1] == 1:
                    perimeter -= 2
                if row > 0 and grid[row - 1][column] == 1:
                    perimeter -= 2
    return perimeter
