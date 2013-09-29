'''
In this programming problem and the next you'll code up the knapsack algorithm
The file describes a knapsack instance, and it has the following format:
[knapsack_size][number_of_items]
[value_1] [weight_1]
[value_2] [weight_2]
...
For example, the third line of the file is "50074 659", indicating that the
second item has value 50074 and size 659, respectively.
You can assume that all numbers are positive. You should assume that item
weights and the knapsack capacity are integers.
'''
import sys
sys.setrecursionlimit(20000)

global knapsack_size
global number_of_items

def get_values_and_weights(filename):
  global knapsack_size
  global number_of_items

  items_to_steal = []
  f = open(filename)

  knapsack_size, number_of_items = [int(x) for x in f.readline().split()]
  for line in f:
    v, w = line.split()
    items_to_steal.append((int(v), int(w)))

  return items_to_steal


# Naive implementation ( bottom-up ) works better for small inputs
def knapsack(items_to_steal):
  # init A with 0
  A = [[0 for _ in xrange(knapsack_size)] for _ in xrange(number_of_items)]

  for i in xrange(number_of_items):
    v, w = items_to_steal[i]
    for x in xrange(knapsack_size):
      if x - w < 0:
        A[i][x] = A[i-1][x]
      else:
        A[i][x] = max(A[i-1][x], A[i-1][x-w] + v)

  return A[number_of_items-1][knapsack_size-1]


# Recursive implementation with memoization ( top-down ) works for large inputs
# Memoization done via python dictionary (hashtable)
def knapsack_memoization(items_to_steal):
    A = {}

    # Return the value of the most valuable subsequence of the first i
    # elements in items whose weights sum to no more than x.
    def get_bestvalue(i, x):
      # init i = 0 col with 0
      if i == 0:
        return 0

      cache_key = str(i)+'-'+str(x)

      if (cache_key) in A:
        return A[cache_key] # memoization

      v, w = items_to_steal[i]
      if x - w < 0:
        result = get_bestvalue(i-1, x)
        A[cache_key] = result # memoization
      else:
        result = max(get_bestvalue(i-1, x), get_bestvalue(i-1, x-w) + v)
        A[cache_key] = result # memoization

      return result

    return get_bestvalue(number_of_items - 1, knapsack_size - 1)


def main():
  # values_and_weights = get_values_and_weights('knapsack1.txt')
  # optimal_solution = knapsack(values_and_weights)

  values_and_weights = get_values_and_weights('knapsack_big.txt')
  optimal_solution = knapsack_memoization(values_and_weights)

  print optimal_solution
main()