from graph import Graph, graph_from_file

filename = "network.test.in"

g = graph_from_file(filename)

print(g)


print(g.connected_components_set())

print(g.get_path_min_dist(1, 4, 11))

print(g.min_power(1, 4))
