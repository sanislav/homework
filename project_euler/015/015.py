'''
Starting in the top left corner of a 2x2 grid, and only being able to move to 
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
'''

# Use Binomial Coeficient https://en.wikipedia.org/wiki/Binomial_coefficient
def use_binomial_coeficient(gridSize):
    paths = 1
    for i in xrange(0, gridSize):
        paths *= (2 * gridSize) - i;
        paths /= i + 1;

    return paths

# Dynamic programming:
def use_dynamic_programming(gridSize):
    # use a gridSize + 1 grid that we initialize with 1 
    grid = [[0 for col in xrange(gridSize + 1)] for row in range(gridSize + 1)]
    # initialize rightmost nodes and bottom line nodes with 1
    for i in xrange(gridSize):
        for j in xrange(gridSize):
            grid[i][gridSize] = 1
            grid[gridSize][j] = 1

    # from any node parsing from bottom right corner towards the top and left
    # the length will be the length of the already calculated paths if we go to
    # the bottom or to the right
    for i in xrange(gridSize-1, -1, -1):
        for j in xrange(gridSize-1, -1, -1):
            grid[i][j] = grid[i+1][j] + grid[i][j+1]
    
    return grid[0][0]

paths = use_binomial_coeficient(20)
print paths
paths = use_dynamic_programming(20)
print paths