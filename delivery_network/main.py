import sys
sys.setrecursionlimit(500000)

from graph import Graph, graph_from_file, time_min_power, sort_edge, kruskal

filename = "input/"
network = "network.9.in"
g = graph_from_file(filename+network)

print(kruskal(g))
