import sys
sys.setrecursionlimit(500000)

from graph import Graph, graph_from_file, time_min_power, kruskal, UnionFind, get_path_in_mst

filename = "input/"
network = "network.00.in"
g = graph_from_file(filename+network)


print(g)
tree = kruskal(g)
print(kruskal(g))

print(get_path_in_mst(tree, 9, 4))

print(g.min_power(9, 4))
