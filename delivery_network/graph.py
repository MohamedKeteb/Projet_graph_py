#"Projet Prog"
from collections import deque
from time import perf_counter
import math
class Graph:
    def __init__(self, nodes=[]):
        self.nodes = nodes
        self.edges = []
        self.power = []
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


# -- 
    def add_edge(self, node1, node2, power, dist=1):
            

        self.graph[node1].append((node2, power, dist))
        self.graph[node2].append((node1, power, dist))
        self.nb_edges += 1
         
 

    
 # Question 2

    def connected_components(self):
        def bfs(start_node, visited):
            component = []
            queue = deque([start_node])
            visited[start_node] = True
            while queue:
                node = queue.popleft()
                component.append(node)
                for neighbor in self.graph[node]:
                    if not visited[neighbor[0]]:
                        visited[neighbor[0]] = True
                        queue.append(neighbor[0])
            return component
        visited = {node:False for node in self.nodes}
        components = []
        for node in self.nodes:
            if not visited[node]:
                component = bfs(node, visited)
                components.append(component)
        return components
    
# fin Q2

    def connected_components_set(self):
        return set(map(frozenset, self.connected_components()))
    

# Question 3
    


    def get_path_with_power(self,src,dest,power):
        queue = deque([(src, [src])])
        visited = set([src])
        while queue:
            node, path = queue.popleft()
            if node == dest:
                return path
            for neighbor in self.graph[node]:
                if neighbor[0] not in visited and power>=neighbor[1]:
                    visited.add(neighbor[0])
                    queue.append((neighbor[0], path + [neighbor[0]]))
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
        c = []
        for i in self.connected_components():
            if src or dest in i:
                c = i
                break
        if src in c and dest in c : 
            p = self.power
            p.sort()
            a = 0
            b = len(p)-1
            m = (a+b)//2
            while a < b :
                if self.get_path_with_power(src,dest,p[m]) != None:
                    b=m
                else:
                    a=m+1
                m=(a+b)//2
            return self.get_path_with_power(src,dest,p[a]),p[a]
        else:
            raise ValueError('Trajet impossible')
    
# Fin Q6

# Question 1 et 4
def graph_from_file(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    nb_nodes, _ = map(int, lines[0].split())
    g = Graph([i for i in range(1, nb_nodes + 1)])
    for i in range(1, len(lines)):
        if len(lines[i].split()) == 3:
            node1, node2, power = map(int, lines[i].split())

            g.add_edge(node1, node2, power)
            g.edges.append((node1, node2, power, 1))
            if power not in g.power:
                g.power.append(power)
        else:
            node1, node2, power, dist = map(int, lines[i].split())
            g.add_edge(node1, node2, power, dist)
            g.edges.append((node1, node2, power, dist))
            if power not in g.power:
                g.power.append(power)
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
        g.min_power(src, dest)

    t_stop = perf_counter()
    
    return (t_stop - t_start)*nb_trajet/10



#Question 3


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        
    def get_parent(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.get_parent(self.parent[x])
        return self.parent[x]
        
    def Union(self, x, y):
        root_x, root_y = self.get_parent(x), self.get_parent(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_x] = root_y
                if self.rank[root_x] == self.rank[root_y]:
                    self.rank[root_y] += 1

#Fin Q3

def kruskal(g):
    if len(g.connected_components_set()) == 1:
        ed = UnionFind(g.nb_nodes)
        i = 0
        edges = g.edges
        edges.sort(key = lambda x : x[2])
        g_mst = Graph(g.nodes)
        while g_mst.nb_edges != g.nb_nodes - 1:
            src, dest, power, dist= edges[i]

            x = ed.get_parent(src - 1)
            y = ed.get_parent(dest - 1)

            if x != y:
                g_mst.add_edge(src, dest, power, dist)
                ed.Union(x, y)

            i+= 1
        return g_mst
    else:
        raise ValueError('g non connexe')


# 4

def get_path_mst(mst,src,dest):
        queue = deque([(src, [(src, -1)])])
        visited = set([src])
        while queue:
            node, path = queue.popleft()
            if node == dest:
                l = path
            for neighbor in mst.graph[node]:
                if neighbor[0] not in visited :
                    visited.add(neighbor[0])
                    queue.append((neighbor[0], path + [(neighbor[0], neighbor[1])]))
        list_power = [l[i][1] for i in range(len(l))]
        powermin = max(list_power)
        min_path = [l[i][0] for i in range(len(l))]

        return min_path, powermin















