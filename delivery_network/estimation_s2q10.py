import sys 
sys.path.append("delivery_network/")

from graph import Graph, graph_from_file, time_min_power
from time import perf_counter

filename = "input/"

for x in range(1, 11):
    network = "network."+str(x)+".in"
    g = graph_from_file(filename+network)
    print('Temps de calcul de routes', x ,' : ', time_min_power(network))
    



    







