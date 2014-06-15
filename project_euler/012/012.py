'''
The sequence of triangle numbers is generated by adding the natural numbers. So 
the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. 

What is the value of the first triangle number to have over five hundred 
divisors?
'''
from math import sqrt

def number_factors(n):
    large_divisors = []
    for i in xrange(1, int(sqrt(n) + 1)):
        if n % i is 0:
            yield i
            if i is not n / i:
                large_divisors.insert(0, n / i)
    for divisor in large_divisors:
        yield divisor

num_divisors = count = triangle_num = 1

while num_divisors <= 500:
    count += 1
    triangle_num += count
    num_divisors = len(list(number_factors(triangle_num)))

print triangle_num
print num_divisors    