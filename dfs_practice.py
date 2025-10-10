from collections import defaultdict

print("DFS Traversal")

edges = int(input("Enter the number of edges: "))

graph = defaultdict(list)

print("Enter the nodes: ")

for _ in range(edges):
    u, v = input().split()
    graph[u].append(v)
    graph[v].append(u)

print(graph)

start = input("Enter the starting node: ")

dfs = list([start])
visited = set()

while dfs:
    cur = dfs.pop()
    if cur not in visited:
        visited.add(cur)
        print(cur, end="->")
        dfs.extend(graph[cur])
