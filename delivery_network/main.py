import sys
sys.setrecursionlimit(500000)

from graph import Graph, graph_from_file, time_min_power, kruskal, UnionFind, ensemble_disj

filename = "input/"
network = "network.05.in"
g = graph_from_file(filename+network)


print(g.edges)


a = [1, 2, 3]


print(a.pop(0))

print(a)