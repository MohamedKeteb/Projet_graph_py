#Projet de Prog
from collections import deque
from time import perf_counter
import numpy as np 
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


    """""
    Description : 
    -----------
    Ajoute une arête sous forme de tuple dans un graph.

    input:
    ------
    node1, node2 : noeuds du graph, type : int
    power : puissance minimale pour passer l'arête, type : int ou float(network.10.in)
    dist : longueur de l'arête qui est par défaut égale à 1 si elle n'est pas renseigné, type : int 

    output:
    ------
    La fonction ne retourne rien
    """


    def add_edge(self, node1, node2, power, dist=1):
            
        # Le graph est non orienté 
        self.graph[node1].append((node2, power, dist))
        self.graph[node2].append((node1, power, dist))
        self.nb_edges += 1

         
    """   Méthode connected_components()
    Description:
    -----------
    la fonction trouve les composantes connexes d'un graph

    input:
    -----
    une instance de Graph

    output:
    -------

    une liste contenant les composantes connexes
        Retourne les composantes connexes du graphe en faisant un parcour en largeure

    """  



 # -----------------------------------------------Question 2

    def connected_components(self):
        def bfs(start_node, visited):
            component = []
            queue = deque([start_node])
            visited[start_node] = True
            while queue:                # la file d’attente contient au moins un noeud, on reste dans la boucle
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
            if not visited[node]:  #on trouves les composantes de tous les noeuds non visités 
                component = bfs(node, visited)
                components.append(component)
        return components
   
# ----------------------------------------------------fin Q2

    """"" Méthode connected_components_set()
    Description:
    -----------
    permet d'nlever les éventuels doublons

    input:
    ------
    Une instance de Graph

    output:
    ------
    un set contenant des frozenset (qui est un set immutable) représentant les composantes connexes

    """

    def connected_components_set(self):
        return set(map(frozenset, self.connected_components()))
    
    """""   Méthode get_path_with_power()
    Description : 
    -----------
    Pour une puissance de camion donnée, renvoie un chemin possible entre deux nœuds, s'il en existe un, None sinon.

    input:
    -----
    src : noeud de départ
    dest : noeud d'arrivée
    power : la puissance du camion

    output:
    -------
    si y a un chemin output = Une liste de noeud (chemin) s'il en existe un. None sinon

    sinon None
    """



# -------------------------------------------------Question 3
    


    def get_path_with_power(self,src,dest,power):
        queue = deque([(src, [src])])
        visited = set([src])
        while queue:
            node, path = queue.popleft()#On envoie le premier tuple de la liste d’attente
            if node == dest:
                return path
            for neighbor in self.graph[node]:
                if neighbor[0] not in visited and power>=neighbor[1]:
                    visited.add(neighbor[0])
                    queue.append((neighbor[0], path + [neighbor[0]]))
        return None

# -------------------------------------------------Fin question3

    """"" Méthode get_path_min_dist()
    Description :
    ------------
    La fonction retourne pour les chemins possibles avec la puissance power, le chemin de distance minimale
    en utilisant l'algorithme de Dijkstra
    input:
    -----
    src: noeud de départ 
    dest: noeud d'arrivée    
    power: puissance du camion

    output:
    ------
    Si le noeud de départ et d'arrivée ne sont pas des composantes connexe, la fonction renvoie None
    sinon sinon la méthode renvoie un couple contenant le chemin et la puissance.
    """



# --------------------------------------Question 5 avec Dijkstra:

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
            node, dist_node = to_visit.pop()
            if not visited[node]:
                visited[node] = True 
                for v in self.graph[node] :
                    dist_v = dist_node + v[2]
                    if dist_v < distance[v[0]] and power >= v[1]: # Dans l'alogrithme de Dijkstra il faut mettre la condition sur la puissance 
                        distance[v[0]] = dist_v
                        precedent[v[0]] = node
                        to_visit.append((v[0], dist_v))
            to_visit.sort(reverse=True)

        if distance[dest] == math.inf:
            return None
        else :     
            return chem(dest), distance[dest]
    
    """"" Méthode : min_power()
    Description:
    ------------
    Renvoie le chemin ainsi que la avec la puissance minimale nécessaire pour aller d’un nœud de départ à un nœud d’arrivée,
    s’il en existe un, en utilisant une recherche binomiale (i.e un parcours dichotomique. La fonction renvoie une erreur sinonsi c'est possible 
    La méthode min_power réalise une dichotomie sur la liste des puissances répertoriées entre deux nœuds. 
    input:
    -----
    src: noeud de départ
    dest: noeud d'arrivée
    output:
    ------
    si pas de chemin : soulever une erreur 
    sinon return une couple contenant contant le chemin sous forme de liste et la puissance minimale sous la forme d’un str.
    """
# ----------------------------------------------Fin Q5
        

# ----------------------------------------Question6 

    def min_power(self, src, dest):
        if self.get_path_with_power(src, dest, float('inf')) != None: # on vérifie qu'un chemin existe.
            p = self.power
            p.sort() # on trie les puissance pour faire une dichotomie 
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
    
# -----------------------------------------------------Fin Q6

    

# --------------------------------------------------Question 1 et 4


    """""   Fonction : graph_from_file()
    Description:
    ------------
    crée un graph à partir d'un fichier network

    input:
    -----
    filename : Chemin du fichier contenant le graph

    output:
    -------
    une instance de la classe Graph

    """

def graph_from_file(filename):
    with open(filename, "r") as file:
        n, m = map(int, file.readline().split())
        g = Graph(range(1, n+1))
        for _ in range(m):
            edge = file.readline().split()
            if len(edge) == 3: # on distingue les cas ou la puissance n'est pas renseignée
                node1, node2, power_min = int(edge[0]),int(edge[1]),int(edge[2])
                g.add_edge(node1, node2, power_min) # will add dist=1 by default
                g.edges.append((node1, node2, power_min,1))
                g.power.append(power_min)
            elif len(edge) == 4:
                node1, node2, power_min, dist = int(edge[0]),int(edge[1]),int(edge[2]),float(edge[3]) #Pour pouvoir lire 10
                g.add_edge(node1, node2, power_min, dist)
                g.edges.append((node1, node2, power_min,dist))
                g.power.append(power_min)
            else:
                raise Exception("Format incorrect")
    return g




# ----------------------------------------------FIN q1 et Q4

    
# Question8 ---> Dans le ficier test_s1q8 dans tests








#---------------------------------------------------Séance 2 

"""""   Fonction : time_min_power
Description:
------------
A partir d'un fichier représentant un graph on donne un estimation du temps qu'il faudrait pour calculer 
les trajets du fichier route associé.

input:
-----
network: le fichier contenant le graph

output:
-------
un temps 


"""


#-----------------------------------------------Question 10 
# Voir le fichier texte temps.min.power

def time_min_power(network):
    filename = r"C:\Users\keteb\OneDrive\Bureau\ensae-prog23\input/"+ network
    g = graph_from_file(filename)
    x = network.split('.')[1]

    f = open(r"C:\Users\keteb\OneDrive\Bureau\ensae-prog23\input/"+ 'routes.' + str(x) + '.in', 'r')
    lines = f.readlines()

    nb_trajet = len(lines)

    t_start  = perf_counter()

    for i in range(1, 6): # on prend 5 trajets 
        src, dest, _ = map(float, lines[i].split())
        g.min_power(src, dest)

    t_stop = perf_counter()
    return (t_stop-t_start)*nb_trajet/5

#-------------------------------------------------Fin Q10



#----------------------------------------------Question 12

"""""   Class UnionFind
Attributs : 
-----------
parent : liste
rank : liste 

Methodes : 
----------

get_parent(): obtenir le parent d'un noeud qui est un représentant d'un groupe de noeuds
Union(): permet de réunir deux groupes de noeuds
"""

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n)) # on initialise une liste où chaque noeud est son prpre parent
        self.rank = [0] * n
        
    def get_parent(self, x):    # Retrouver le représentant de x pendant la construction de l'arbre couvrant 
        if self.parent[x] != x:
            self.parent[x] = self.get_parent(self.parent[x])
        return self.parent[x]
        
    def Union(self, x, y):  # réunir deux groupes en réunissant le représentant de x et de y.
        root_x, root_y = self.get_parent(x), self.get_parent(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_x] = root_y
                if self.rank[root_x] == self.rank[root_y]:
                    self.rank[root_y] += 1

"""""   Fonction : kruskal
Description:
-----------
Permet d'envoyer un objet de la Class Graph qui est un arbre couvrant de poids minimal.
input:
------
g : une instance de la classe graph

output:
-------
une instance de la classe graph

"""

def kruskal(g):
    if len(g.connected_components_set()) == 1:
        ed = UnionFind(g.nb_nodes)
        i = 0
        edges = g.edges
        edges.sort(key = lambda x : x[2])
        g_mst = Graph(g.nodes)
        while g_mst.nb_edges != g.nb_nodes - 1:
            src, dest, power, dist= edges[i]

            x = ed.get_parent(src - 1) # les noeuds sont numérotés de 1 à n on fait -1 pour pouvoir applique 
            # union find qui est implémenté pour les graphs numérotés à partir de 0
            y = ed.get_parent(dest - 1)

            if x != y:  # si les représentants sont diffétents on raccroche les deux composantes de x et y 
                g_mst.add_edge(src, dest, power, dist)
                ed.Union(x, y)

            i+= 1
        return g_mst
    else:
        raise ValueError('g non connexe')

#---------------------------------------------Fin Q12




#--------------------------------------------Question 14

"""""   Fonction : build_oriented_tree
Description: 
-----------
La fonction prend un arbre orienté et le transforme en un arbre orienté des enfants vers le parents 

Input: tree
------
tree : Arbre non orienté, instance de la Class Graph
root : racine voulu pour l'arbre, root = 1 par défaut


output:
-------
Arbre orienté des enfants vers les parents
"""

def build_oriented_tree(tree, root=1):
        # Construire un arbre orienté des enfants vers les parents avec un BFS
        oriented_tree = {root: []}
        queue = deque([root])
        visited = {root}
        while queue:
            parent = queue.popleft()
            for child in tree.graph[parent]:
                if child[0] not in visited:
                    visited.add(child[0])
                    oriented_tree[child[0]] = [(parent,child[1],child[2])]
                    queue.append(child[0])
        return oriented_tree


"""""   Fonction : get_path
Description:
-----------
trouve le chemin entre deux noeuds dans un arbre en remontant les ancêtres pour touver 
l'ancêtre minimum

Input:
------
src : noeud de départ
type : int

dest : noeud d'arrivée
type : int

tree : arbre orienté des enfants vers le parents

output : 
-------

un couple contenant la puissance minimal et le chemin de src à dest
"""
def min_power_tree(src, dest, tree):
    src_ancestors = []
    curr = src
    while curr != 1: # on récupère les ancêtres de src
        src_ancestors.append([curr, tree[curr][0][1]])
        curr = tree[curr][0][0]
    src_ancestors.append([1, 0])
    dest_ancestors = []
    curr = dest
    while curr != 1: # on récupère les ancêtres de dest
        dest_ancestors.append([curr, tree[curr][0][1]])
        curr = tree[curr][0][0]
    dest_ancestors.append([1, 0])

    # Trouver l'indice du premier ancêtre commun entre src et dest
    i = len(src_ancestors) - 1
    j = len(dest_ancestors) - 1
    while i >= 0 and j >= 0 and src_ancestors[i][0] == dest_ancestors[j][0]:
        i -= 1
        j -= 1

    # Concaténer les chemins de src et dest jusqu'à l'ancêtre commun
    path = src_ancestors[:i+2]
    path[i+1][1] = 0
    path.extend(reversed(dest_ancestors[:j+1]))

    return max([x[1] for x in path]), [x[0] for x in path]

"""""   Fonction : time_min_power_tree
Description :
------------
A partir d'un graph et d'un arbre couvrant, la fonction retourne le temps de calcul 
de min_power_tree() sur les fichiers routes
input:
-----
network: le nom du graph ex: network.1.in
tree: l'arbre couvrant minimal

output:
------
un temps 

"""

#-------------------------------------------------QuestionQ15



def time_min_power_tree(network, tree):
    x = network.split('.')[1]

    f = open(r"C:\Users\keteb\OneDrive\Bureau\ensae-prog23\input/"+ 'routes.' + str(x) + '.in', 'r')
    lines = f.readlines()

    nb_trajet = len(lines)
    t_start  = perf_counter()

    for i in range(1, nb_trajet):
        src, dest, _ = map(float, lines[i].split())
        min_power_tree(src, dest, tree)

    t_stop = perf_counter()
    
    return (t_stop - t_start)


#-----------------------------------Q16


""""" Fonction: process
Description:
------------
on crée un dictionnaire avec tous les ancêtres à une distance d'une puissance de 2
et on répertorie les puissance minimlaes pour atteindres ces ancêstres

input:
------
tree: arbre couvrant minimal donné par kruskal mais orienté des enfants vers les parents.

output:
-------
up: dictionnaire

"""

def process(tree):
# tree orienté des enfants vers les parents
    N=len(tree)
    up={k: [(-1,0) for i in range(int(math.log2(N))+1)] for k in tree.keys()} 
    for v in tree.keys():
        up[v][0]=(tree[v][0][0],tree[v][0][1])
    for j in range(1,int(math.log2(N))+1):
        for v in tree.keys():
            if up[v][j-1][0]!=-1 and up[up[v][j-1][0]][j-1][0]!=-1:
                up[v][j]=up[up[v][j-1][0]][j-1][0],max(up[v][j-1][1],up[up[v][j-1][0]][j-1][1])  # ces deux conditions permettent de ne pas sortir de l'arbre dans le premier et le deuxième saut
    return up # une relation de récurrence montre que pour atteindre l'ancêtre 
                        # à 2^j on prend le 2^j-1 ancêtre du 2^j-1 ème ancêtre.

    
"""""   Fonction level
Description recherche de la profondeur de chaque noeuds en utilisant un BFS.
input: 
arbre couvrant minimal donné par kruskal
output:
dictionnaire contenant toutes les profondeures

"""

def level(tree): # non orienté
    lv = { k : 0 for k in tree.graph.keys()}
    q = deque([1])
    visited = {1}
    while q:
        current_node = q.popleft()
        for neighbors in tree.graph[current_node]:
            if neighbors[0] not in visited:
                visited.add(neighbors[0]) 
                lv[neighbors[0]] = lv[current_node] + 1
                q.append(neighbors[0])
    return lv

"""""   Fonction find_lca
Description:
----------
on cherche l'ancêtre commun minimal de a et b (qui sont des neouds), mais on remonte 
aux ancêtres avec des puissance de 2 donc plus rapidement.

input:
-------
lv: dictionnaire des profondeurs
up: dictionnaire du préprocessing
a: noeud de départ 
b: noued d'arrivée

output:
-------
puissance minimal pour relier a et b.

"""

def min_power_lca(a, b, up, lv): 
    p = [0]
    n = len(lv)
    if lv[a] < lv[b]:
        a, b = b, a
    c = a
    for i in range(int(math.log2(n)), -1, -1): # permet de se placer à la même profondeur 
        if lv[c] - 2**i >= lv[b]:

            p = p + [up[c][i][1]]
            
            c = up[c][i][0]
    if c == b:
        return max(p)
    for i in range(int(math.log2(n)), -2, -1):
        if up[b][i][0] != -1 and  up[b][i][0] != up[c][i][0]:

            p = p + [up[b][i][1]] # on stock les puissances 
            p = p + [up[c][i][1]]

            b =  up[b][i][0]
            c = up[c][i][0]
    p = p + [up[c][0][1], up[b][0][1]]
    return max(p)



#----------------------------------Question17
#cf fichier temps_S3q17 dans delivery_network.


"""""   Fonction time_find_lca()
même fonction que que pour time_min_power_tree() mais cette fois pour la fonction 
min_power_lca()

"""


def time_min_power_lca(network, up, lv):
    x = network.split('.')[1]

    f = open(r"C:\Users\keteb\OneDrive\Bureau\ensae-prog23\input/"+ 'routes.' + str(x) + '.in', 'r')
    lines = f.readlines()

    nb_trajet = len(lines)
    t_start  = perf_counter()

    for i in range(1, nb_trajet):
        src, dest, _ = map(float, lines[i].split())
        min_power_lca(src, dest, up, lv)

    t_stop = perf_counter()
    
    return (t_stop - t_start)
        


#---------------------------------------------------Question 18-----------------------------------------------------

