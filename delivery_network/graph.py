#"Projet Prog"
from time import perf_counter
import math
class Graph:
    def __init__(self, nodes=[]):
        self.nodes = nodes
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
        self.min_edge= float('inf')
        self.max_edge = 0 
    


    def __str__(self):
        """Prints the graph as a list of neighbors for each node (one per line)"""
        if not self.graph:
            output = "The graph is empty"            
        else:
            output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n"
            for source, destination in self.graph.items():
                output += f"{source}-->{destination}\n"
        return output
    
    def update(self, power):
        if power <= self.min_edge:
            self.min_edge = power
        if power >= self.max_edge:
            self.max_edge = power


    def add_edge(self, node1, node2, power, dist=1):
        self.update(power)
        k = self.graph.keys()
        if node1 not in k:
            self.graph[node1] = [(node2, power, dist)]
        else : 
            self.graph[node1].append((node2, power, dist))

        if node2 not in k:
            self.graph[node2] = [(node1, power, dist)]
        else : 
            self.graph[node2].append((node1, power, dist))
         
    def neig(self, node):
        return [j[0] for j in self.graph.get(node)]  

    def deep_parcour(self,node,l):
        if node not in l:
            l.append(node)
            for w in self.neig(node):
                self.deep_parcour(w, l)
        return l 
 # Question 2

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
    

# Question 3
    def get_path_with_power(self,src,dest,power):
        pile = [(src, [src], set())]
        while pile:
            node, path, visited = pile.pop()
            visited.add(node)
            if node == dest:
                return path
            for neighbor in self.graph[node]:
                if neighbor[0] not in visited and power>=neighbor[1]:
                    pile.append((neighbor[0], path + [neighbor[0]], visited.copy()))
        return None

# Fin question3
 
#Question 4 avec Q1




# Question 5 avec Dijkstra

    def get_path_min_dist(self, src, dest, power):
        
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
            return chem(dest), distance[dest]
        

# Q 6 min power par dichotomie

    def min_power(self, src, dest):
            a = self.min_edge
            b = self.max_edge
            m = (a+b)//2
            while a < b :
                if self.get_path_with_power(src,dest,m) != None:
                    b=m
                else:
                    a=m+1
                m=(a+b)//2
            return self.get_path_with_power(src,dest,a),a
    
# Fin Q6

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




    
# Question8 dans le ficier test_s1q8








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

    for i in range(1, 10):
        src, dest, _ = map(int, lines[i].split())
        g.min_power_bis(src, dest)

    t_stop = perf_counter()
    
    return (t_stop - t_start)*nb_trajet/10


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
   
       
    



#Fin Q3

#Question 4 
#Fin Question 4 



# Q5

def min_power_mst(g, src, dest):
    mst_g = kruskal(g)
    def deep_parcour_mst(self,node,l):
        if node not in l:
            l.append(node)
            for w in self.neig(node):
                self.deep_parcour(w, l)
        return l 
    pass

    




## get_path_with_power DFS 



