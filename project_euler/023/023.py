'''
A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However, this upper limit
cannot be reduced any further by analysis even though it is known that the
greatest number that cannot be expressed as the sum of two abundant numbers is
less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.
'''
from math import sqrt


def number_factors(n):
    for i in xrange(1, int(sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i != n / i and i != 1:
                yield n / i


if __name__ == "__main__":
    abundant_numbers = [
        i for i in xrange(12, 28124) if sum(list(number_factors(i))) > i]

    # keep sums in a hash table so that lookups are O(1)
    abundant_sums = {i + j: ''
                     for i in abundant_numbers for j in abundant_numbers}

    print sum(i for i in xrange(1, 28124) if i not in abundant_sums)
