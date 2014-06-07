# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

def sum_matrix_cells(matrix):
  num_lines = len(matrix)
  num_cols  = len(matrix[0])

  carried_value = 0 
  big_sum_str   = ''
  for i in range(num_cols -1 , -1, -1) :
    sum_col = 0
    for j in range(num_lines-1, -1, -1) :
      # add digits on the same col
      sum_col += matrix[j][i]

    sum_col       += int(carried_value)
    # we carry on whatever remains in the sum after keeping the last digit
    carried_value = str(sum_col)[:-1]

    # just keep the last digit if we didn't reach the end
    if i != 0 : 
      big_sum_str += str(sum_col)[-1]
    else :
      big_sum_str += str(sum_col)[::-1]

  # string must be reversed in order to get the correct answer
  print big_sum_str[::-1][0:10]  

def generate_digits_matrix(filename):
  f = open(filename)
  full_numbers = [line.split() for line in f]
  digits = []
  
  # represent each number as a list where each position in the list
  # corresponds to a digit from the number.
  # we end up with a matrix each line representing a number 
  for i in range(0, len(full_numbers)) :
    number_digits = []
    for j in full_numbers[i][0] :
      number_digits.append(int(j))
    digits.append(number_digits)
  
  return digits

matrix = generate_digits_matrix('numbers.txt')
sum_matrix_cells(matrix)