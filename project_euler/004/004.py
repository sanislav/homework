def largest_palindrome():
  largest = 0
  for i in range(999, 100, -1) :
    for j in range(999, 100, -1) :
      prod = i * j
      if is_palindrome(prod) :
        if largest < prod :
          largest = prod

  return largest      

def is_palindrome(n):
  to_str = str(n)
  if to_str == to_str[::-1] :
    return True

  return False  

print largest_palindrome()