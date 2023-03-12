import sys
from time import perf_counter

sys.setrecursionlimit(500000)

from graph import Graph, graph_from_file, time_min_power, kruskal, build_oriented_tree, get_path

filename = "input/"
network = "network.1.in"

g = graph_from_file(filename + network)

mst2 = kruskal(g)
tree2 = build_oriented_tree(mst2)

print(tree2)



