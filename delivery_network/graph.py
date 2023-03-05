
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
    
    def add_edge(self, node1, node2, power_min, dist=1):
        k = self.graph.keys()
        if node1 not in k:
            self.graph[node1] = [(node2, power_min, dist)]
        else : 
            self.graph[node1].append((node2, power_min, dist))

        if node2 not in k:
            self.graph[node2] = [(node1, power_min, dist)]
        else : 
            self.graph[node2].append((node1, power_min, dist))
         
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
            return chem


# Question 5
    def get_path_min_dist(self, src, dest, power):
        les_chemins = self.get_all_path_with_power(src, dest, power)
        def dist_trip(l): 
            d = 0   
            for i in range(len(l)-1):
                for j in g.graph[l[i]]:
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





   




# Question 1 et 4
def graph_from_file(filename):
    g = Graph()
    f = open(filename, 'r')
    lines = f.readlines()
    g.nb_nodes, g.nb_edges = map(int, lines[0].split())
    g.nodes = [i for i in range(1, g.nb_nodes + 1)]
    g.graph = dict([(n, []) for n in g.nodes])
    for i in range(1, len(lines)):
        if len(lines[i].split()) == 3:
            node1, node2, power_min = map(int, lines[i].split())
            g.add_edge(node1, node2, power_min)
        else:
            node1, node2, power_min, dist = map(int, lines[i].split())
            g.add_edge(node1, node2, power_min, dist)
    return g




    









#Séance 2 

#Question 3

def sort_edge(g):
    edge = []
    for v in g.graph.keys(): 
        for e in g.graph[v]:
            if (e[0], v, e[1]) in edge:
                continue
            edge.append((v, e[0], e[1]))
    edge.sort(key= lambda x: x[2])
    return edge

def kruskal(g):
    tree = Graph(g.nodes)
    array = g.nodes
    edge  = sort_edge(g)
    while array != [edge[0][0]]*g.nb_nodes:
        for a in edge:
            if array[a[0] - 1] != array[a[1] - 1]:
                array[a[0] - 1] = array[a[1] - 1]
                tree.graph[a[0]], tree.graph[a[1]] = a[1], a[0]           
    return tree.graph



