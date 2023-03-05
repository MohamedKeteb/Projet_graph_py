from graph import Graph, graph_from_file

filename = "network.test.in"

g = graph_from_file(filename)

print(g)


print(g.connected_components_set())

print(g.min_power(1, 2))


