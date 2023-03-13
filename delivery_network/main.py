



#%%
import sys
from time import perf_counter

sys.setrecursionlimit(500000)

from graph import Graph, graph_from_file, time_min_power, kruskal, build_oriented_tree, min_power_tree

file = r"C:\Users\keteb\OneDrive\Bureau\ensae-prog23\delivery_network\comparaison_temps_calcul"
f = open(file, 'w')
f.write("temps de calcul : min_power Q6    min_power_tree Q14\n")

for x in range(1, 11):
    network = "network."+str(x)+".in"
    f.write("           "+str(time_min_power(network))+"     "+"         "+"\n")

f.close()

#%%

import sys
from time import perf_counter

sys.setrecursionlimit(500000)

from graph import Graph, graph_from_file, time_min_power, kruskal, build_oriented_tree, min_power_tree
from generate_output import oriented_tree

file = r"C:\Users\keteb\OneDrive\Bureau\ensae-prog23\delivery_network\comparaison_temps_calcul"

filename1 = 'network.1.in'
filename2 = 'network.2.in'
filename3 = 'network.3.in'
filename4 = 'network.4.in'
filename5 = 'network.5.in'
filename6 = 'network.6.in'
filename7 = 'network.7.in'
filename8 = 'network.8.in'
filename9 = 'network.9.in'
filename10 = 'network.10.in'

tree1 = oriented_tree(filename1).tree
tree2 = oriented_tree(filename2).tree
tree3 = oriented_tree(filename3).tree
tree4 = oriented_tree(filename4).tree
tree5 = oriented_tree(filename5).tree
tree6 = oriented_tree(filename6).tree
tree7 = oriented_tree(filename7).tree
tree8 = oriented_tree(filename8).tree
tree9 = oriented_tree(filename9).tree
tree10 = oriented_tree(filename10).tree

print(1)

f = open(file, 'w')
f.write("")
network = "network."+str(1)+".in"
f.write("           "+"             "+"   "+str(time_min_power(network, tree1))+"\n")

f.close()

print(2)








# %%
