from graph import Graph, graph_from_file, get_path_with_power, get_path_with_power_dist, min_power

filename = "network.test.in"

g = graph_from_file(filename)

print(g)

print(g.connected_components_set())
print(g.get_path_with_p(1, 2, 11))

