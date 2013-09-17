'''In this programming problem and the next you'll code up the clustering
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

# Create a list of tuples dict with keys = eges as tuples (node1, node2) and val
# the weight of the edge
def represent_edge_weights():
  global nr_nodes
  count = 0
  graph = {}
  # for line in open('test.txt', 'r'):
  for line in open('clustering1.txt', 'r'):
    vals = line.split()
    if(count > 0):
      graph.update({ (int(vals[0]), int(vals[1])) : int(vals[2])})
      graph.update({ (int(vals[1]), int(vals[0])) : int(vals[2])})
    else:
      nr_nodes = int(vals[0])
    count += 1

  return graph


# initially each node belongs to it's own cluster. represent clusters as
# {node: ([leader vertexes])}
def init_clusters(nr_nodes):
  clusters = {}
  for i in xrange(1, nr_nodes + 1):
    clusters.update({i : set([i])})

  return clusters


# given a node return the group it belongs to
def get_lead_node(clusters, node):
  for lead, nodes in clusters.iteritems():
    if node in nodes:
      return lead


# return the cluster leads that have the closest distance between them
def get_min_distance_clusters(graph, clusters, nr_nodes, group_clusters):
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
          if (node, other_node) in graph:
            # get weight and retain it if < current smallest one
            w = graph.get((node, other_node))
            if w <= closest_distance:
              closest_distance = w
              closest_clusters = (get_lead_node(clusters, node),get_lead_node(clusters, other_node))

  if ( group_clusters == 1 ):
    return closest_clusters
  else:
    return closest_distance


# merge cluster a in cluster b. will merge the small one into the larger one
def merge_clusters(clusters, cluster_a_lead, cluster_b_lead):
  cluster_a = clusters.get(cluster_a_lead)
  cluster_b = clusters.get(cluster_b_lead)

  # move nodes of cluster b into cluster a and delete cluster b
  if len(cluster_a) < len(cluster_b):
    min_cluster, max_cluster, min_cluster_lead = cluster_a, cluster_b, cluster_a_lead
  else:
    min_cluster, max_cluster, min_cluster_lead = cluster_b, cluster_a, cluster_b_lead

  for i in min_cluster:
    if i not in max_cluster:
      max_cluster.add(i)

  del(clusters[min_cluster_lead])

  return clusters


def group_clusters(graph, nr_nodes):
  clusters  = init_clusters(nr_nodes)
  while len(clusters) > 4:
    # get min distance between 2 clusters and merge these 2 into 0
    min_distance_clusters = get_min_distance_clusters(graph, clusters, nr_nodes, 1)

    # merge the 2 clusters into 1. the smaller one gets a leader update
    clusters = merge_clusters(clusters, min_distance_clusters[0], min_distance_clusters[1])

  return clusters


def main():
  global nr_nodes
  # parse the file and create a list of dict with keys = tuples (e1,e2) and
  # value the weight of the edge
  graph     = represent_edge_weights()

  grouped_clusters = group_clusters(graph, nr_nodes)
  print 'The 4 closest clusters are %s' % grouped_clusters

  # get max distance between the 4 clusters
  furthest_distance = get_min_distance_clusters(graph, grouped_clusters, nr_nodes, 0)
  print 'The max spacing of the 4 clusters is %d' % furthest_distance


if __name__ == '__main__':
  main()
