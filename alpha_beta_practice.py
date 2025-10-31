from collections import defaultdict

print("Alpha Beta Pruning")


def collect_subtree(node, tree, nodes):
    nodes.append(node)
    for child in tree[node]:
        collect_subtree(child, tree, nodes)


def alpha_beta(node, alpha, beta, is_max, tree, pruned, level=0):
    if node not in tree:
        return int(node)

    print(f"{'    ' * level}Level: {level}-> Node:{node}, Alpha:{alpha}, Beta: {beta}")

    if is_max:
        value = -float("inf")
        for child in tree[node]:
            if value >= beta:
                branch = []
                collect_subtree(child, tree, branch)
                pruned.extend(branch)
                continue
            val = alpha_beta(child, alpha, beta, False, tree, pruned, level + 1)
            value = max(value, val)
            alpha = max(alpha, value)
        return value
    else:
        value = float("inf")
        for child in tree[node]:
            if value <= alpha:
                branch = []
                collect_subtree(child, tree, branch)
                pruned.extend(branch)
                continue
            val = alpha_beta(child, alpha, beta, True, tree, pruned, level + 1)
            value = min(value, val)
            beta = min(beta, value)
        return value


def print_tree(tree, node):
    children = tree.get(node, [])
    if children:
        print(f"{node}: {children}")
    else:
        print(f"{node}: Leaf Node")

    for child in children:
        print_tree(tree, child)


tree = defaultdict(list)

n = int(input("Enter the number of edges: "))
print("Enter the node and it's child: ")
for _ in range(n):
    u, v = input().split()
    tree[u].append(v)
print(tree)

root = list(tree.keys())[0]
pruned = []
final_value = alpha_beta(root, -float("inf"), float("inf"), True, tree, pruned)

print("Original Tree:")
print_tree(tree, root)

print("Pruned Nodes: ", pruned)
print("Final Value: ", final_value)


"""
a b
a c
b d
b e
d 2
d 3
c f 
c g 
f 0 
f 1
g 7 
g 5
e 5 
e 9
"""

