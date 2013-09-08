"""In this programming problem and the next you'll code up the greedy algorithms
from lecture for minimizing the weighted sum of completion times.. Download
the text file here. This file describes a set of jobs with positive and
integral weights and lengths. It has the format
[number_of_jobs]
[job_1_weight] [job_1_length]
[job_2_weight] [job_2_length]
...

For example, the third line of the file is "74 59", indicating that the second
job has weight 74 and length 59. You should NOT assume that edge weights or
lengths are distinct.

1. Your task in this problem is to run the greedy algorithm that schedules jobs in
decreasing order of the difference (weight - length). Recall from lecture that
this algorithm is not always optimal. IMPORTANT: if two jobs have equal
difference (weight - length), you should schedule the job with higher weight
first. Beware: if you break ties in a different way, you are likely to get the
wrong answer.

2.For this problem, use the same data set as in the previous problem. Your task
now is to run the greedy algorithm that schedules jobs (optimally) in decreasing
order of the ratio (weight/length). In this algorithm, it does not matter how you
break ties.
"""


# Create a list of tuples (weight, length)
def create_weights_and_lengths_lists():
  jobs = []
  count = 0
  for line in open('greedy.txt', 'r'):
    if(count > 0):
      vals = line.split()
      jobs.append((int(vals[0]), int(vals[1])))
    count += 1

  return jobs


# Sort list of tuples
def schedule_jobs(jobs, greedy_rule, handle_ties):
  jobs.sort(key = handle_ties)
  jobs.sort(key = greedy_rule)
  return jobs


def sum_of_weighted_completion_times( jobs ):
  time  = 0
  sum   = 0
  for w, l in jobs:
    time  += l
    sum   += w * time

  return sum


def main():
  # parse the file and create a list of tuples [(w1,l1)...]
  jobs = create_weights_and_lengths_lists()

  # order by weight - length in decending order.
  # will not be optimal and should yeld a > reult than greedy_2
  greedy_1    = lambda tuple: -(tuple[0] - tuple[1])

  # sort by w / l in descending order
  greedy_2    = lambda tuple: -float(tuple[0])/tuple[1]  # always correct

  # for ties sort by weight in descending order
  handle_ties = lambda tuple: -tuple[0]

  # sort jobs
  jobs = schedule_jobs( jobs, greedy_1, handle_ties )
  print 'Greedy w - l: %i' % sum_of_weighted_completion_times(jobs)

  jobs = schedule_jobs( jobs, greedy_2, handle_ties )
  print 'Greedy w / l: %i' % sum_of_weighted_completion_times(jobs)

if __name__ == '__main__':
  main()

