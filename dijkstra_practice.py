from collections import defaultdict
import heapq


distances = {}
path = defaultdict(list)


def initialize_distances(graph, start):
    global distances
    for node in graph:
        distances[node] = float("inf")
    distances[start] = 0


def dijkstra(graph, start):
    global distances
    initialize_distances(graph, start)
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        curr_dist, curr_node = heapq.heappop(pq)

        if curr_dist > distances[curr_node]:
            continue

        for neigh, weight in graph[curr_node]:
            new_dist = curr_dist + weight
            if new_dist < distances[neigh]:
                distances[neigh] = new_dist
                path[neigh] = path[curr_node] + [curr_node]
                heapq.heappush(pq, (new_dist, neigh))


graph = defaultdict(list)

edges = int(input("Enter the number of edges: "))
for _ in range(edges):
    inp = input("Enter nodes with distances: ")
    u, v, w = inp.split()
    graph[u].append((v, int(w)))
    graph[v].append((u, int(w)))

start = input("Enter the starting edge: ")
dijkstra(graph, start)


print(f"Shortest distance of each node from start node {start}: ")
for node in graph:
    path[node].append(node)
    print(f"{start} -> {node}:{distances[node]} {path[node]}")
