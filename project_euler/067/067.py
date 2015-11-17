'''
By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle in the file triangle.txt
'''


'''
Idea is to read from bottom up and calculate for every last 2
rows which paths are worth keeping.

We do this by calculating all possible sums for 2 lines and keeping the largest
sum for each possible path we can take. In our example from 2 we can either go
to 8 or 5. The largest sum is 10. From 4 we can go to 5 or 9. Largest sum in
this case is 13. From 6 to 9 or 3 the sum is 15.

So by 'crunching' the last 2 lines we end up with the line of maximum sums i.e.
10 13 15.

Triangle becomes:
    3
  7  4
10 13 15

Step 2 triangle becomes:
   3
20   19

Step 3 triangle becomes the largest sum: 23
'''


# create a list of lists each list representing a line in the triangle
# order it in reverse order (order in which they will be processed)
def parse_file_into_list(file_name):
    lines = []
    for line in reversed(open(file_name).readlines()):
        line_list = [int(num) for num in line.rstrip().split(' ')]
        lines.append(line_list)

    return lines


# given 2 lists of n and n+1 elements calculate the max sums for each combination
# possible (as explained above) and return the resulting list of length n
def crunch_lists(list_one, list_two):
    crunched_list = []
    # list_two is bigger than list_one by 1 element
    for index, val in enumerate(list_two):
        local_sum = max(val + list_one[index], val + list_one[index + 1])
        crunched_list.append(local_sum)

    return crunched_list


def get_sum_of_maximum_path():
    lines = parse_file_into_list('triangle.txt')
    # parse the lines and calculate the sums
    while len(lines) > 1:
        crunched_lines = crunch_lists(lines[0], lines[1])
        # remove first 2 lists (lines) from original list and add the crunched list
        lines.pop(0)
        # second item now becomes first
        lines.pop(0)

        # set crunched list as first element
        lines.insert(0, crunched_lines)

    return lines[0][0]

print get_sum_of_maximum_path()
