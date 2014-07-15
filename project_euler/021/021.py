'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n 
which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and 
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 
142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

from math import sqrt

# generate proper divisors 
def number_factors(n):
    large_divisors = []
    for i in xrange(1, int(sqrt(n) + 1)):
        if n % i is 0:
            yield i
            if i is not n / i and i is not 1:
                large_divisors.insert(0, n / i)

    for divisor in large_divisors:
        yield divisor

amicable = []
for a in xrange(2,10001):
    if a not in amicable:
        d_a = sum(list(number_factors(a)))
        d_b = sum(list(number_factors(d_a)))

        if a == d_b and a != d_a:
            amicable.append(a)
            amicable.append(d_a)

print amicable
print sum(amicable)