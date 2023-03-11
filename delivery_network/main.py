import sys
from time import perf_counter

sys.setrecursionlimit(500000)

from graph import Graph, graph_from_file, time_min_power, kruskal, UnionFind, get_path_mst

filename = "input/"
network = "network.00.in"
#g = graph_from_file(filename+network)



print(time_min_power('network.2.in'))






