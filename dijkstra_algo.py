'''
Dijkstra Shortest Path algorithm
'''

def shortest_path(n: int, edges: List[List[int]], source: int) -> Dict[int, int]:
    adjacency = {}
    for i in range(n):
        adjacency[i] = []

    # src - source
    # dest - destination node
    for src, dest, weight in edges:
        adjacency[src].append([dest, weight])
    
    shortest = {}  # Map vertex -> dist of the shortest path

    min_heap = [[0, source]]
    while min_heap:
        weight1, node1 = heapq.heappop(min_heap)
        if node1 in shortest:
            continue
        shortest[node1] = weight1

        for node2, weight2 in adjacency[node1]:
            if node2 not in shortest:
                heapq.heappush(min_heap, [weight1 + weight2, node2])

    for i in range(n):
        if i not in shortest:
            shortest[i] = -1

    return shortest
