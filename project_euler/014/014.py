# The following iterative sequence is defined for the set of positive integers:
# n = n/2 (n is even)
# n = 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

lengths_dict = {1:1}
def do_collatz(number) :
    # keep calculated path for the current number
    # when we reach a number from where we already calculated
    # the path length STOP.
    current_stack = []
    while number != 1 :
        while number not in lengths_dict :
            current_stack.append(number)
            if number % 2: 
                number = 3 * number + 1
            else :
                number = number / 2
            
            # check if we should continue to calculate collatz
            # or if we already did this for this number
            if number in lengths_dict :
                # already calculated this path -> add all current path elements
                # to the dict of lengths
                for index, val in enumerate(current_stack) :
                    lengths_dict[val] = len(current_stack[index:]) + lengths_dict[number]
                break
        break
    return True

for i in xrange(1,10**6) :
    do_collatz(i)

max_length      = 0
searched_num    = 0
for i in lengths_dict :
    if lengths_dict[i] > max_length :
        max_length = lengths_dict[i]
        searched_num = i

print max_length
print searched_num
