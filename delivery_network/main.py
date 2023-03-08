from graph import Graph, graph_from_file, time_min_power, sort_edge

filename = "network.test.in"

g = graph_from_file(filename)

print(g)

print(sort_edge(g))
