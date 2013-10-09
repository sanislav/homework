'''
In this programming problem and the next you'll code up the clustering
algorithm from lecture for computing a max-spacing k-clustering. This file
describes a distance function (equivalently, a complete graph with edge costs).
It has the following format:
[number_of_nodes]
[edge 1 node 1] [edge 1 node 2] [edge 1 cost]
[edge 2 node 1] [edge 2 node 2] [edge 2 cost]
...
There is one edge (i,j) for each choice of 1 <= i < j <= n, where n is the
number of nodes. For example, the third line of the file is "1 3 5250",
indicating that the distance between nodes 1 and 3 (equivalently, the cost of
the edge (1,3)) is 5250. You can assume that distances are positive, but you
should NOT assume that they are distinct.

Your task in this problem is to run the clustering algorithm from lecture on
this data set, where the target number k of clusters is set to 4. What is the
maximum spacing of a 4-clustering?

Shit's too slow. Needs improvement. Takes about 1m:15s
A: 106
'''

infinity = 10000000
global nr_nodes
global nodes_and_leaders

def MakeSet(x):
  x.parent = x
  x.rank   = 0

def Union(x, y):
  xRoot = Find(x)
  yRoot = Find(y)
  if xRoot.rank > yRoot.rank:
    yRoot.parent = xRoot
  elif xRoot.rank < yRoot.rank:
    xRoot.parent = yRoot
  elif xRoot != yRoot: # Unless x and y are already in same set, merge them
    yRoot.parent = xRoot
    xRoot.rank = xRoot.rank + 1

def Find(x):
  if x.parent == x:
    return x
  else:
    x.parent = Find(x.parent)
  return x.parent



# Create a list of tuples dict with keys = eges as tuples (node1, node2) and val
# the weight of the edge
def represent_edges_and_weights():
  global nr_nodes
  f = open('test.txt')

  nr_nodes = [int(x) for x in f.readline().split()][0]

  # init the matrix
  M = [[None for i in xrange(nr_nodes + 1)] for j in xrange(nr_nodes + 1)]

  for line in f:
    e1, e2, w = line.split()
    M[int(e1)][int(e2)] = M[int(e2)][int(e1)] = int(w)

  return M


# initially each node belongs to it's own cluster. represent clusters as
# {node: ([leader vertexes])}
def init_clusters(nr_nodes):
  global nodes_and_leaders
  clusters  = {}
  nodes_and_leaders = {}

  for i in xrange(1, nr_nodes + 1):
    clusters.update({i : set([i])})
    # each node points to it's own leader
    nodes_and_leaders.update({i:i})
  return clusters


# return the cluster leads that have the closest distance between them
def get_min_distance_clusters(graph, clusters, nr_nodes, group_clusters):
  global nodes_and_leaders
  closest_clusters = (0,0)
  closest_distance = infinity
  all_nodes = xrange(1, nr_nodes + 1)

  for cluster in clusters:
    nodes_in_cluster = clusters.get(cluster)
    # for each node in current cluster compare with the nodes in all other
    # clusters
    for node in nodes_in_cluster:
      # retain min distance between 2 clusters. i.e. min distance between any
      # node of 1 cluster with the ones from the other clusters
      for other_node in all_nodes:
        # compare with nodes from other clusters only
        if other_node not in nodes_in_cluster:
          # get node - other_node weight
          edge = (0,0)
          if (node, other_node) in graph:
            edge = (node, other_node)
          if (other_node, node) in graph:
            edge = (other_node, node)

          if edge[0] != 0:
            # get weight and retain it if < current smallest one
            w = graph.get(edge)
            if w <= closest_distance:
              closest_distance = w
              # get the 2 lead nodes of the clusters
              closest_clusters = (edge[0], edge[1])

  if ( group_clusters == 1 ):
    return closest_clusters
  else:
    return closest_distance


# merge cluster a in cluster b. will merge the small one into the larger one
def merge_clusters(clusters, cluster_a_lead, cluster_b_lead):
  global nodes_and_leaders
  cluster_a = clusters.get(cluster_a_lead)
  cluster_b = clusters.get(cluster_b_lead)

  # move nodes of cluster b into cluster a and delete cluster b
  if len(cluster_a) < len(cluster_b):
    min_cluster, max_cluster, min_cluster_lead, max_cluster_lead = cluster_a, cluster_b, cluster_a_lead, cluster_b_lead
  else:
    min_cluster, max_cluster, min_cluster_lead, max_cluster_lead = cluster_b, cluster_a, cluster_b_lead, cluster_a_lead

  for i in min_cluster:
    if i not in max_cluster:
      max_cluster.add(i)
      # update leaders of i
      nodes_and_leaders[i] = max_cluster_lead

  del(clusters[min_cluster_lead])
  # print nodes_and_leaders
  return clusters


def group_clusters(graph, nr_nodes):
  print graph
  clusters  = [MakeSet(node) for node in graph]
  print clusters
  # while len(clusters) > 4:
  #   # get min distance between 2 clusters and merge these 2 into 0
  #   min_distance_clusters = get_min_distance_clusters(graph, clusters, nr_nodes, 1)

  #   # merge the 2 clusters into 1. the smaller one gets a leader update
  #   clusters = merge_clusters(clusters, min_distance_clusters[0], min_distance_clusters[1])

  # return clusters


def main():
  global nr_nodes
  # parse the file and create a matrix like M[v1][v2] = M[v2][v1] = weight of edge v1-v2
  matrix = represent_edges_and_weights()

  # grouped_clusters = group_clusters(graph, nr_nodes)
  # print 'The 4 closest clusters are %s' % grouped_clusters

  # # get max distance between the 4 clusters
  # furthest_distance = get_min_distance_clusters(graph, grouped_clusters, nr_nodes, 0)
  # print 'The max spacing of the 4 clusters is %d' % furthest_distance


if __name__ == '__main__':
  main()
