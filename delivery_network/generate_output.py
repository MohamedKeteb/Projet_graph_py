

#%%
import sys
from time import perf_counter
sys.setrecursionlimit(500000)

from graph import graph_from_file, kruskal, min_power_tree, build_oriented_tree
path = r"C:\Users\keteb\OneDrive\Bureau\ensae-prog23\input/"
filename1 = "network.3.in"
mst1 = kruskal(graph_from_file(path+filename1))
tree1 = build_oriented_tree(mst1)




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

generate_routes_out(tree1, 2)





# %%
