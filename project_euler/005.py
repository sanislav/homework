# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def smallest_divisible(n):
  # small optimization we start with what we know to be 
  # the smallest to divide 1-10
  smallest_divisible = 2520

  # if it's divisible by 10 it must end in 0
  # that means it's also divisible by 2, 5 so no need to check those 
  # if it's divisible by 2 and 3 then it's also divisible by 6
  # if it's divisible by 3 and 4 then it's also divisible by 11
  # if it's divisible by 3 and 5 then it's also divisible by 15
  # if it's divisible by 2 and 9 then it's also divisible by 18
  to_check = [3,4,7,8,9,11,13,14,16,17,19,20] 
  # iterate using a step of 10
  while 1 :
    smallest_divisible += 10
    # divisible by 2,5 and 10
    for j in to_check :
      # bail out if not divisible
      if smallest_divisible % j != 0 :
        break
      # divisible by all numbers (we reached 19) then return 
      if j == to_check[-1] :
        return smallest_divisible 

print smallest_divisible(20)

### OR ###

# Compute the prime factorization of each number from 1 to 20, 
# and multiply the greatest power of each prime together:

# 20 = 2^2 * 5
# 19 = 19
# 18 = 2 * 3^2
# 17 = 17
# 16 = 2^4
# 15 = 3 * 5
# 14 = 2 * 7
# 13 = 13
# 11 = 11
print 2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19