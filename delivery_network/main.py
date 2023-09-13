



#%%
import sys
from time import perf_counter

sys.setrecursionlimit(500000)

from graph import Graph, graph_from_file, time_min_power, kruskal, build_oriented_tree, min_power_tree
# construire le fichier temps.min.power
file = r"C:\Users\keteb\OneDrive\Bureau\ensae-prog23\delivery_network\temps.min_power"
f = open(file, 'w')
f.write("temps de calcul : min_power Q6\n")

for x in range(1, 11):
    network = "network."+str(x)+".in"
    t = time_min_power(network)
    f.write("routes"+str(x)+": "+str(t)+"sec = "+str(t/60)+"min"+"\n")

f.close()


#%%
import sys
from time import perf_counter

sys.setrecursionlimit(500000)
from graph import Graph, graph_from_file, time_min_power, kruskal, build_oriented_tree, min_power_tree, level, min_power_lca, process

g = graph_from_file(r"C:\Users\keteb\OneDrive\Bureau\ensae-prog23\input\network.2.in")
tree = kruskal(g)
ot = build_oriented_tree(tree)
print(1)
print(level(tree))
print(process(ot))


# %%


from graph import preprocessing, greddy
def trucks_filter(filename_trucks):
    with open (filename_trucks, 'r') as file:
        nb_trucks = int(file.readline())
        trucks = []
        for _ in range(nb_trucks):
            power, cost = file.readline().split()
            trucks.append((int(power), int(cost)))
    file.close()

    trucks.sort(key = lambda x: (x[0], -x[1]))
    trucks_filter = [trucks[-1]]
    for elt in trucks[-2::-1]:
        if elt[1] < trucks_filter[-1][1]:
            trucks_filter.append(elt)
    return trucks_filter[::-1]

filename_trucks = r'C:\Users\keteb\OneDrive\Bureau\Projet_graph_py\input\trucks.2.in'

t = trucks_filter(filename_trucks)

filename = 'output\routes.1.out'
print(preprocessing(filename, t))








# %%
