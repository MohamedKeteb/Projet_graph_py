#"Projet Prog"
from time import perf_counter
import math
class Graph:
    def __init__(self, nodes=[]):
        self.nodes = nodes
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
    


    def __str__(self):
        """Prints the graph as a list of neighbors for each node (one per line)"""
        if not self.graph:
            output = "The graph is empty"            
        else:
            output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n"
            for source, destination in self.graph.items():
                output += f"{source}-->{destination}\n"
        return output
    
    def add_edge(self, node1, node2, power, dist=1):
        k = self.graph.keys()
        if node1 not in k:
            self.graph[node1] = [(node2, power, dist)]
        else : 
            self.graph[node1].append((node2, power, dist))

        if node2 not in k:
            self.graph[node2] = [(node1, power, dist)]
        else : 
            self.graph[node2].append((node1, power, dist))
         
 # Question 2
    def neig(self, node):
        return [j[0] for j in self.graph.get(node)]  

    def deep_parcour(self,node,l):
        if node not in l:
            l.append(node)
            for w in self.neig(node):
                self.deep_parcour(w, l)
        return l 

    def connected_components(self):
        visited = [False] * self.nb_nodes
        component = []
        for i in range(self.nb_nodes):
            if not visited[i] : 
                component.append(self.deep_parcour(i+1, l=[]))
                for j in self.deep_parcour(i+1, l = []):
                    visited[j-1] = True 
        return component
# fin Q2

    def connected_components_set(self):
        return set(map(frozenset, self.connected_components()))
    
# Question3
    def get_path_with_power(self, src, dest, power):
        def arret(l, dest):
            for i in l:
                if i[-1] is not dest : 
                    return False
            return True 
        c = []
        for l in self.connected_components():
            if src in l:
                c = l
        if dest not in c:
            return None
                
        chem = [[src]]
        while not arret(chem, dest):
            q = []
            for p in chem:
                u = p[-1]
                if u == dest:
                    q.append(p)
                else:
                    for t in self.graph[u]:
                        if not (t[0] in p) and power>= t[1]:
                            v = [i for i in p]
                            v.append(t[0])
                            q.append(v)
            chem= q
        if len(chem) == 0:
            return None
        else:
            return chem[0]
# Fin Q3

# Question 3 avec Dijkstra

    def dijk(self, src, dest, power):
        
        def chem(i):
            chemin = [i]
            while i != src:
                chemin.append(precedent[i])
                i = precedent[i]
            chemin.reverse()
            return chemin


        precedent = {x: None for x in self.graph.keys()}
        visited = {x : False for x in self.graph.keys()}
        distance = {x : math.inf for x in self.graph.keys()}
        distance[src] = 0
        to_visit = [(src, 0)]
        while to_visit:
            print(to_visit)
            node, dist_node = to_visit.pop()
            if not visited[node]:
                visited[node] = True 
                for v in self.graph[node] :
                    dist_v = dist_node + v[2]
                    if dist_v < distance[v[0]] and power >= v[1]:
                        distance[v[0]] = dist_v
                        precedent[v[0]] = node
                        to_visit.append((v[0], dist_v))
            to_visit.sort(reverse=True)

        if distance[dest] == math.inf:
            return None
        else :     
            return chem(dest)
        





    def get_all_path_with_power(self, src, dest, power):
        def arret(l, dest):
            for i in l:
                if i[-1] is not dest : 
                    return False
            return True 
        c = []
        for l in self.connected_components():
            if src in l:
                c = l
        if dest not in c:
            return None
                
        chem = [[src]]
        while not arret(chem, dest):
            q = []
            for p in chem:
                u = p[-1]
                if u == dest:
                    q.append(p)
                else:
                    for t in self.graph[u]:
                        if not (t[0] in p) and power>= t[1]:
                            v = [i for i in p]
                            v.append(t[0])
                            q.append(v)
            chem= q
        if len(chem) == 0:
            return None
        else:
            return chem()


# Question 5
    def get_path_min_dist(self, src, dest, power):
        assert self.get_all_path_with_power(src, dest, power) != None, "Puissance insuffisante pour couvrir le Trajet!!!"
        les_chemins = self.get_all_path_with_power(src, dest, power)
        def dist_trip(l): 
            d = 0   
            for i in range(len(l)-1):
                for j in self.graph[l[i]]:
                    if j[0] == l[i+1]:
                        d += j[2]
            return d
        d_min = min([dist_trip(l) for l in les_chemins])
        les_chemins_min = []
        for t in les_chemins:
            if dist_trip(t) == d_min:
                les_chemins_min.append(t)
        return les_chemins_min, d_min
    
# Fin Q5


# Question 6

    def min_power(self, src, dest):
        def power_trip(l): 
            w = 0   
            for i in range(len(l)-1):
                for j in self.graph[l[i]]:
                    if j[0] == l[i+1] and j[1] >= w:
                        w = j[1]            
            return w

        les_chemins_min = []
        les_chemins = self.get_all_path_with_power(src, dest, power = math.inf)
        p_min = min([power_trip(l) for l in les_chemins])
        for l in les_chemins:
            if power_trip(l) == p_min:
                les_chemins_min.append(l)
        return les_chemins_min, p_min
    
# Fin Q6

# Q 6 min power par dichotomie

    def min_power_bis(self, src, dest):
        
            i=0
            while self.get_path_with_power(src,dest,2**i) == None:
                i+=1
            l = [j for j in range(2**i+1)]
            a = 0
            b = len(l)-1
            m = (a+b)//2
            while a < b :
                if self.get_path_with_power(src,dest,l[m]) != None:
                    b=m
                else:
                    a=m+1
                m=(a+b)//2
            return self.get_path_with_power(src,dest,l[a]),a





   




# Question 1 et 4
def graph_from_file(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    nb_nodes, nb_edges = map(int, lines[0].split())
    g = Graph([i for i in range(1, nb_nodes + 1)])
    g.nb_edges = nb_edges
    for i in range(1, len(lines)):
        if len(lines[i].split()) == 3:
            node1, node2, power = map(int, lines[i].split())
            g.add_edge(node1, node2, power)
        else:
            node1, node2, power, dist = map(int, lines[i].split())
            g.add_edge(node1, node2, power, dist)
    return g




    









#Séance 2 


#Question 1 

def time_min_power(network):
    filename = "input/"+ network
    g = graph_from_file(filename)
    x = network.split('.')[1]

    f = open("input/"+ 'routes.' + str(x) + '.in', 'r')
    lines = f.readlines()

    nb_trajet = len(lines)

    t_start  = perf_counter()

    for i in range(1, 3):
        src, dest, _ = map(int, lines[i].split())
        g.min_power(src, dest)

    t_stop = perf_counter()
    
    return (t_start - t_stop)*nb_trajet/2


#Question 3

def sort_edge(g):
    edge = []
    for v in g.graph.keys(): 
        for e in g.graph[v]:
            if (e[0], v, e[1], e[2]) in edge:
                continue
            edge.append((v, e[0], e[1], e[2]))
    edge.sort(key= lambda x: x[2])
    return edge

class ensemble_disj:

    parent = {}
    def __init__(self, N):
        for i in range(N):
            self.parent[i] = i
    def get_represent(self, k):
        if self.parent[k] == k:
            return k
        return self.get_represent(self.parent[k])
    def union(self, a, b):
        x = self.get_represent(a)
        y = self.get_represent(b)
        self.parent[x] = y

def kruskal(g):
    ed = ensemble_disj(g.nb_nodes)
    i = 0
    edge = sort_edge(g)
    g_mst = Graph(g.nodes)
    tree = []
    while len(tree) != g.nb_nodes - 1:
        src, dest, power, dist= edge[i]

        x = ed.get_represent(src - 1)
        y = ed.get_represent(dest - 1)

        if x != y:

            tree.append(edge[i])
            g_mst.graph[src].append((dest, power, dist ))
            g_mst.graph[dest].append((src, power, dist ))
            ed.union(x, y)
        i+= 1
    return g_mst






