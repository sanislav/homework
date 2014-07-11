'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
'''

import math


def is_prime(n):
    if n == 2 or n == 3:
        return True

    if n%2 == 0 or n%3 == 0:
        return False

    # only check if it's divisible with numbers < sqrt(n) ofc.
    upper_limit = int(math.ceil(math.sqrt(n)))
    for i in xrange(5, upper_limit + 1):
        if n%i == 0:
            return False

    return True

# start checking from 3 and only check odd numbers
# 2 is prime so we anlready know 1st prime
nth_prime = 1
check_num = 3
max_nth_prime = 10001
while nth_prime < max_nth_prime:
    if is_prime(check_num):
        nth_prime += 1
    
    # next number we check is odd
    if nth_prime < max_nth_prime:
        check_num += 2

print check_num