'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

def get_triples(triples_sum):
    for a in xrange(triples_sum, 2, -1):
        for b in xrange(a, triples_sum):
            c = triples_sum - a - b

            if c**2 == a**2 + b**2:
                return [a, b, c]

    return False

print reduce(lambda x, y: x * y, get_triples(1000))
