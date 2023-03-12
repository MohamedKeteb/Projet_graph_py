
#%%
import sys 
sys.path.append("delivery_network/")
from time import perf_counter
from graph import Graph, graph_from_file, time_min_power, min_power_tree
from generate_output import oriented_tree

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
#tree2 = oriented_tree(filename2).tree
#tree3 = oriented_tree(filename3).tree
#tree4 = oriented_tree(filename4).tree
#tree5 = oriented_tree(filename5).tree
#tree6 = oriented_tree(filename6).tree
#tree7 = oriented_tree(filename7).tree
#tree8 = oriented_tree(filename8).tree
#tree9 = oriented_tree(filename9).tree
#tree10 = oriented_tree(filename10).tree


#%%


def time_min_power_tree(network):
    filename = "input/"+ network
    g = graph_from_file(filename)
    x = network.split('.')[1]

    f = open("input/"+ 'routes.' + str(x) + '.in', 'r')
    lines = f.readlines()
    n = f.readlines()
    t_start  = perf_counter()

    for i in range(int(n)):
        src, dest, _ = map(int, lines[i].split())
        min_power_tree(src, dest, tr)

    t_stop = perf_counter()
    return (t_stop - t_start)


filename = "input/"
path = "C:\Users\keteb\OneDrive\Bureau\ensae-prog23\delivery_network\comparaison_temps_calcul"
f = open(path, 'w')
f.write("temps de calcul : min_power Q6    min_power_tree Q14 ")
for x in range(1, 11):
    network = "network."+str(x)+".in"
    g = graph_from_file(filename+network)
    f.write("           "+time_min_power(network)+"     "+time_min_power(network)+"\n")
    