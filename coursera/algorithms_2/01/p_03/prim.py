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

from collections import defaultdict
import random

def convert_data_to_adjacency_list():
  f = open('edges.txt')
  f.readline().split()

  # nodes, edges = [int(x) for x in f.readline().split()]
  adjacency_list = defaultdict(list)

  for line in f:
    start_node, end_node, cost = [int(x) for x in line.split()]
    adjacency_list[start_node].append([end_node, cost])
    adjacency_list[end_node].append([start_node, cost])

  return adjacency_list


# Get MST and it's cost using the naive implementation
# TODO : the heap version
def prim(adjacency_list):
  num_nodes = len(adjacency_list)
  X = []
  MST = []
  MST_with_cost = []
  total_cost_of_MST = 0

  # get a random node and initialize X with this
  s = random.randint(1, num_nodes)
  X.append(s)

  while len(X) < num_nodes:
    edge = (0,0)
    # init cheapest edge with 'infinity'
    cheapest_cost = 10000000

    for explored_node in X:
      # parse every edge that has a node in the current node from X called explored_node
      for end_node, cost in adjacency_list.get(int(explored_node)):
        # if not already added as the cheapest edge and it's cost is cheaper than previously discovered
        if (int(explored_node), int(end_node)) not in MST and (int(end_node), int(explored_node)) not in MST and cost < cheapest_cost and end_node not in X:
          cheapest_cost = cost
          edge = (int(explored_node), int(end_node))

    total_cost_of_MST += cheapest_cost
    X.append(edge[1])
    MST.append(edge)

  MST_with_cost.append(total_cost_of_MST)
  MST_with_cost.append(MST)

  return MST_with_cost



def main():
  adjacency_list = convert_data_to_adjacency_list()

  MST = prim(adjacency_list)

  print "The cost of the MST is: %i" % MST[0]

if __name__ == '__main__':
  main()
