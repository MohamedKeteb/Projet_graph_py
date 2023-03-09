from graph import Graph, graph_from_file, time_min_power, sort_edge, kruskal

filename = "network.test.in"

g = graph_from_file(filename)

print(g)

print(g.dijk(2, 3, 6))