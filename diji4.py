graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'C': 6, 'D': 1},
    'C': {'A': 5, 'B': 6, 'D': 3, 'E': 8},
    'D': {'B': 1, 'C': 3, 'E': 4},
    'E': {'C': 8, 'D': 4}
}

unvisited = list(graph.keys())
dist = {node: float('inf') for node in graph}
dist['A'] = 0

while unvisited:
    node = min(unvisited, key=lambda n: dist[n])
    unvisited.remove(node)
    for neigh, w in graph[node].items():
        if dist[neigh] > dist[node] + w:
            dist[neigh] = dist[node] + w

print("Shortest distances from A:")
for node, d in dist.items():
    print(f"A -> {node} = {d}")
