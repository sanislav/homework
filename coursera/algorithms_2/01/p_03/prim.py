'''In this programming problem you'll code up Prim's minimum spanning tree
algorithm. Download the text file here. This file describes an undirected graph
with integer edge costs. It has the format
[number_of_nodes] [number_of_edges]
[one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]
[one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]
...
For example, the third line of the file is "2 3 -8874", indicating that there is
an edge connecting vertex #2 and vertex #3 that has cost -8874. You should NOT
assume that edge costs are positive, nor should you assume that they are
distinct.

Your task is to run Prim's minimum spanning tree algorithm on this graph. You
should report the overall cost of a minimum spanning tree --- an integer,
which may or may not be negative.'''

# Create a list of tuples (weight, length)
def create_weights_and_lengths_lists():
  jobs = []
  count = 0
  for line in open('jobs.txt', 'r'):
    if(count > 0 ):
      vals = line.split()
      jobs.append( (int(vals[0]), int(vals[1])) )
    count += 1

  return jobs


def main():
  # parse the file and create a list of tuples [(w1,l1)...]
  jobs = create_weights_and_lengths_lists()

if __name__ == '__main__':
  main()
