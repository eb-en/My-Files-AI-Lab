from itertools import permutations


def read_input():
    n = int(input("Enter number of cities: "))
    city_names = []
    names = input("Enter the city names: ")
    city_names.extend(x for x in names.split())

    graph = []
    for i in range(n):
        row = []
        for j in range(n):
            val = int(
                input(f"Enter the distance from {city_names[i]} to {city_names[j]}: ")
            )
            row.append(val)
        graph.append(row)

    start_city = input("Enter start city: ")
    start_index = city_names.index(start_city)
    return graph, city_names, start_index


def tsp(graph, city_names, start):
    n = len(graph)
    cities = list(range(n))
    cities.remove(start)
    min_cost = float("inf")
    min_path = []
    for perm in permutations(cities):
        curr_cost = 0
        k = start
        path = [start]
        for j in perm:  # perm = (0,1,3,4)
            curr_cost += graph[k][j]
            k = j
            path.append(j)
        curr_cost += graph[k][start]
        path.append(start)
        if curr_cost < min_cost:
            min_cost = curr_cost
            min_path = path
    named_path = [city_names[i] for i in min_path]
    return named_path, min_cost


graph, city_names, start_city = read_input()
path, cost = tsp(graph, city_names, start_city)
print("\nShorted path: ", "->".join(path))
print("Min Cost: ", cost)
