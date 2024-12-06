#!/usr/bin/python3
'''Define the perimeter of island described in grid'''


def island_perimeter(grid):
    '''
    Returns the perimeter of island decribed in grid
    Args:
        grid is a list of list of integers
    Return: perimeter of island
        0 represents water
        1 represents land
        Each cell is square, with a side length of 1
        Cells are connected horizontally/vertically (not diagonally)
    '''
    if not grid or not grid[0]:
        return 0
    row, col = len(grid), len(grid[0])
    perimeter = 0

    for r in range(row):
        for c in range(col):
            if grid[r][c] == 1:
                perimeter += 4
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2
    return perimeter
