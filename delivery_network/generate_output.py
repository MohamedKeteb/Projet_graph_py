

#%%
import sys
from time import perf_counter
sys.setrecursionlimit(500000)

from graph import graph_from_file, kruskal, min_power_tree, build_oriented_tree, time_min_power_tree, time_min_power
path = r"C:\Users\keteb\OneDrive\Bureau\ensae-prog23\input/"

class oriented_tree:
    def __init__(self, filename):
        self.mst = kruskal(graph_from_file(path+filename))
        self.tree = build_oriented_tree(self.mst)

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


# %%

path_in = r"C:\Users\keteb\OneDrive\Bureau\ensae-prog23\input/"
path_out = r"C:\Users\keteb\OneDrive\Bureau\ensae-prog23\delivery_network/"


def generate_routes_out(tree,x):
    f=open(path_out+"routes."+str(x)+".out","w")  
    with open(path_in+"routes."+str(x)+".in","r") as file:
        n=file.readline()
        f.write(n)
        for _ in range(int(n)):
            src,dest,utility=file.readline().split()
            p=str(min_power_tree(int(src),int(dest), tree)[0])
            f.write(src+" "+dest+" "+utility+" "+p+"\n") 
    f.close()

generate_routes_out(tree1, 1)
generate_routes_out(tree2, 2)
generate_routes_out(tree3, 3)
generate_routes_out(tree4, 4)
generate_routes_out(tree5, 5)
generate_routes_out(tree6, 6)
generate_routes_out(tree7, 7)
generate_routes_out(tree8, 8)
generate_routes_out(tree9, 9)
generate_routes_out(tree10, 10)








# %%
file = r"C:\Users\keteb\OneDrive\Bureau\ensae-prog23\delivery_network\temps.min_power_tree"

f = open(file, 'w')
f.write("temps de calcul : min_power_tree Q14\n")

t = time_min_power_tree(path_in+filename1, tree1)
f.write('routes1 : '+str(t)+'sec = '+str(t/60)+'min\n')

t = time_min_power_tree(path_in+filename2, tree2)
f.write('routes2 : '+str(t)+'sec = '+str(t/60)+'min\n')

t = time_min_power_tree(path_in+filename3, tree3)
f.write('routes3 : '+str(t)+'sec = '+str(t/60)+'min\n')

t = time_min_power_tree(path_in+filename4, tree4)
f.write('routes4 : '+str(t)+'sec = '+str(t/60)+'min\n')

t = time_min_power_tree(path_in+filename5, tree5)
f.write('routes5 : '+str(t)+'sec = '+str(t/60)+'min\n')

t = time_min_power_tree(path_in+filename6, tree6)
f.write('routes6 : '+str(t)+'sec = '+str(t/60)+'min\n')

t = time_min_power_tree(path_in+filename7, tree7)
f.write('routes7 : '+str(t)+'sec = '+str(t/60)+'min\n')

t = time_min_power_tree(path_in+filename8, tree8)
f.write('routes8 : '+str(t)+'sec = '+str(t/60)+'min\n')

t = time_min_power_tree(path_in+filename9, tree9)
f.write('routes9 : '+str(t)+'sec = '+str(t/60)+'min\n')

t = time_min_power_tree(path_in+filename10, tree10)
f.write('routes10 : '+str(t)+'sec = '+str(t/60)+'min\n')

f.close()









# %%
