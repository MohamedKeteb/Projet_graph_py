import sys
from time import perf_counter

sys.setrecursionlimit(500000)

from graph import Graph, graph_from_file, time_min_power, kruskal, UnionFind, get_path_mst, build_oriented_tree, get_path

filename = "input/"
network = "network.00.in"
g = graph_from_file(filename+network)


tree = kruskal(g)

tree_oriented = build_oriented_tree(tree, 1)


print(get_path(7, 4, tree_oriented))

