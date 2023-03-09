from graph import Graph, graph_from_file, time_min_power, sort_edge, kruskal

filename = "network.test.in"
network = "network.1.in"
g = graph_from_file(filename)

print(g)

print(time_min_power(network))