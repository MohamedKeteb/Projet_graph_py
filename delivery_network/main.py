import sys
from time import perf_counter

sys.setrecursionlimit(500000)

from graph import Graph, graph_from_file, time_min_power, kruskal, UnionFind, get_path_mst

filename = "input/"
network = "network.00.in"
g = graph_from_file(filename+network)


print(g)
tree = kruskal(g)

t1 = perf_counter()
print(get_path_mst(tree, 1, 4))
t2 = perf_counter()
print(t2-t1)



v1 = perf_counter()
print(g.min_power(1, 4))
v2 = perf_counter()
print(v2-v1)