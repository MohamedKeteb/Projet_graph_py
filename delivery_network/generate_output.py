

#%%
import sys
from time import perf_counter
sys.setrecursionlimit(500000)

from graph import graph_from_file, kruskal, get_path, build_oriented_tree
path = r"C:\Users\keteb\OneDrive\Bureau\ensae-prog23\input/"
filename1 = "network.1.in"
mst1 = kruskal(graph_from_file(path+filename1))
tree1 = build_oriented_tree(mst1)

filename2 = 'network.2.in'
mst2 = kruskal(graph_from_file(path+filename2))
tree2 = build_oriented_tree(mst2)

filename3 = 'network.3.in'
mst3 = kruskal(graph_from_file(path+filename3))
tree3 = build_oriented_tree(mst3)

filename4 = 'network.4.in'
mst4 = kruskal(graph_from_file(path+filename4))
tree4 = build_oriented_tree(mst4)

filename5 = 'network.5.in'
mst5 = kruskal(graph_from_file(path+filename5))
tree5 = build_oriented_tree(mst5)

filename6 = 'network.6.in'
mst6 = kruskal(graph_from_file(path+filename6))
tree6 = build_oriented_tree(mst6)

filename7 = 'network.7.in'
mst7 = kruskal(graph_from_file(path+filename7))
tree7 = build_oriented_tree(mst7)

filename8 = 'network.8.in'
mst8 = kruskal(graph_from_file(path+filename8))
tree8 = build_oriented_tree(mst8)

filename9 = 'network.9.in'
mst9 = kruskal(graph_from_file(path+filename9))
tree9 = build_oriented_tree(mst9)

filename10 = 'network.10.in'
mst10 = kruskal(graph_from_file(path+filename10))
tree10 = build_oriented_tree(mst10)


# %%
