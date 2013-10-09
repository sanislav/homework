'''In this assignment you will implement one or more algorithms for the
traveling salesman problem, such as the dynamic programming algorithm covered
in the video lectures. Here is a data file describing a TSP instance. The first
line indicates the number of cities. Each city is a point in the plane, and each
subsequent line indicates the x- and y-coordinates of a single city.
The distance between two cities is defined as the Euclidean distance --- that
is, two cities at locations (x,y) and (z,w) have distance
sqrt((x−z)**2+(y−w)**2) between them.

In the box below, type in the minimum cost of a traveling salesman tour for this
instance, rounded down to the nearest integer.'''

def tsp(points):
    #calc all lengths
    all_distances = [[length(x,y) for y in points] for x in points]
    #initial value - just distance from 0 to every other point + keep the track of edges
    A = {(frozenset([0, idx+1]), idx+1): (dist, [0,idx+1]) for idx,dist in enumerate(all_distances[0][1:])}
    cnt = len(points)
    for m in range(2, cnt):
        B = {}
        for S in [frozenset(C) | {0} for C in itertools.combinations(range(1, cnt), m)]:
            for j in S - {0}:
                B[(S, j)] = min( [(A[(S-{j},k)][0] + all_distances[k][j], A[(S-{j},k)][1] + [j]) for k in S if k != 0 and k!=j])  #this will use 0th index of tuple for ordering, the same as if key=itemgetter(0) used
        A = B
    res = min([(A[d][0] + all_distances[0][d[1]], A[d][1]) for d in iter(A)])
    return res[1]