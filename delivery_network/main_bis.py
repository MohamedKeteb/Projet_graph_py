from graph import preprocessing, greedy, dynamique
def trucks_filter(filename_trucks):
    with open (filename_trucks, 'r') as file:
        nb_trucks = int(file.readline())
        trucks = []
        for _ in range(nb_trucks):
            power, cost = file.readline().split()
            trucks.append((int(power), int(cost)))
    file.close()

    trucks.sort(key = lambda x: (x[0], -x[1]))
    trucks_filter = [trucks[-1]]
    for elt in trucks[-2::-1]:
        if elt[1] < trucks_filter[-1][1]:
            trucks_filter.append(elt)
    return trucks_filter[::-1]

filename_trucks = r'C:\Users\keteb\OneDrive\Bureau\Projet_graph_py\input\trucks.0.in'

t = trucks_filter(filename_trucks)



filename = r'C:\Users\keteb\OneDrive\Bureau\Projet_graph_py\output\routes.1.out'
sac = preprocessing(filename, t)

#print(greddy(sac))







