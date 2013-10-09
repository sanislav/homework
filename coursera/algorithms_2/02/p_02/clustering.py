'''In this question your task is again to run the clustering algorithm from
lecture, but on a MUCH bigger graph. So big, in fact, that the distances (i.e.,
edge costs) are only defined implicitly, rather than being provided as an
explicit list.
The format is:
[# of nodes] [# of bits for each node's label]
[first bit of node 1] ... [last bit of node 1]
[first bit of node 2] ... [last bit of node 2]
...
For example, the third line of the file
"0 1 1 0 0 1 1 0 0 1 0 1 1 1 1 1 1 0 1 0 1 1 0 1" denotes the 24 bits associated
with node #2.

The distance between two nodes u and v in this problem is defined as the Hamming
distance--- the number of differing bits --- between the two nodes' labels. For
example, the Hamming distance between the 24-bit label of node #2 above and the
label "0 1 0 0 0 1 0 0 0 1 0 1 1 1 1 1 1 0 1 0 0 1 0 1" is 3 (since they differ
  in the 3rd, 7th, and 21st bits).

The question is: what is the largest value of k such that there is a
k-clustering with spacing at least 3? That is, how many clusters are needed to
ensure that no pair of nodes with all but 2 bits in common get split into
different clusters?

NOTE: The graph implicitly defined by the data file is so big that you probably
can't write it out explicitly, let alone sort the edges by cost. So you will
have to be a little creative to complete this part of the question. For example,
is there some way you can identify the smallest distances without explicitly
looking at every pair of nodes?'''


'''Idea: Since the question requires clustering with spacing of at least 3, we
only need to find out the edges with cost 0, 1 and 2, and then do the union-find
against them.

So for each node that we read generate all possible nodes that are at distance <
2. This means 300 variations per node. With these generated nodes check if they
are in the list of nodes. If a match is found do the clustering. At the end count
the number of clusters.
'''

from union_find import *

def parse_nodes() :
  count = 0
  uf = UnionFind()

  for line in open('clustering_big.txt', 'r'):
  # for line in open('test.txt', 'r'):
    if count >= 1:
      line = line.replace(' ', '')
      node_id = line.split()[0]

      # map node id (binary) to node number (converted to int)
      if uf.find(node_id) == None:
        uf.insert_objects({node_id:node_id})

        # for each node get all possible nodes that are within a hamming
        # distance < 3
        node_variations = hamming(node_id, 1) + hamming(node_id, 2)

        for alt_node_id in node_variations:
          # check if these generated variations are found in our data
          original_leader = uf.find(alt_node_id)
          if original_leader != None:

            new_leader      = uf.find(node_id)

            if new_leader != original_leader:
              # update the leader of nodes in the cluster with the found node
              to_change_leader_nodes = uf.find(original_leader)
              unchanged_leader_nodes = uf.find(new_leader)

              uf.union(to_change_leader_nodes, unchanged_leader_nodes)

    count +=1

  print len(uf.num_weights)


def flip(c):
  return str(1-int(c))

def flip_s(s, i):
   t =  s[:i]+flip(s[i])+s[i+1:]
   return t

def hamming(s, k):
  if k>1:
    c = s[-1]
    s1 = [y+c for y in hamming(s[:-1], k)] if len(s) > k else []
    s2 = [y+flip(c) for y in hamming(s[:-1], k-1)]
    r = []
    r.extend(s1)
    r.extend(s2)
    return r
  else:
    return [flip_s(s,i) for i in range(len(s))]


if __name__ == '__main__':
  parse_nodes()
