'''
Starting in the top left corner of a 2x2 grid, and only being able to move to 
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
'''

# Use Binomial Coeficient https://en.wikipedia.org/wiki/Binomial_coefficient

gridSize = 20
paths = 1
for i in xrange(0, gridSize):
    paths *= (2 * gridSize) - i;
    paths /= i + 1;

print paths