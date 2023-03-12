import sys
from time import perf_counter

sys.setrecursionlimit(500000)

from graph import Graph, graph_from_file_bis, time_min_power, kruskal, build_oriented_tree, min_power_tree

filename = "input/"
network = "network.3.in"

g = graph_from_file_bis(filename + network)
print(g)







