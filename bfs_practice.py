from collections import defaultdict, deque

print("BFS Traversal")

edges = int(input("Enter the number of edges: "))

graph = defaultdict(list)

print("Enter the nodes: ")

for _ in range(edges):
    u, v = input().split()
    graph[u].append(v)
    graph[v].append(u)

print(graph)

start = input("Enter the starting node: ")

bfs = deque([start])
visited = set()

while bfs:
    cur = bfs.popleft()
    if cur not in visited:
        visited.add(cur)
        print(cur, end="->")
        bfs.extend(graph[cur])
