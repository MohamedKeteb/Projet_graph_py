from graph import preprocessing, greedy, dynamique, trucks_filter


filename_trucks = r'C:\Users\keteb\OneDrive\Bureau\Projet_graph_py\input\trucks.1.in'

t = trucks_filter(filename_trucks)
print(t)
filename = r'C:\Users\keteb\OneDrive\Bureau\Projet_graph_py\output\routes.1.out'
sac = preprocessing(filename, t)












