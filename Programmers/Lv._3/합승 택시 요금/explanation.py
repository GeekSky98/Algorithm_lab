from collections import defaultdict
from heapq import heappush, heappop
def dijkstra(node_num, start, graph):
    dist = {node: float('inf') for node in range(1, node_num+1)}
    dist[start] = 0
    queue = [(0, start)]

    while queue:
        cost, node = heappop(queue)
        for target, fare in graph[node]:
            new_cost = cost + fare
            if new_cost < dist[target]:
                dist[target] = new_cost
                heappush(queue, (new_cost, target))

    return dist

def solution(n, s, a, b, fares):
    graph = defaultdict(list)
    for node1, node2, fare in fares:
        graph[node1].append((node2, fare))
        graph[node2].append((node1, fare))

    center = dijkstra(n, s, graph)
    a_map = dijkstra(n, a, graph)
    b_map = dijkstra(n, b, graph)

    answer = float('inf')
    for i in range(1, n+1):
        total_cost = center[i] + a_map[i] + b_map[i]
        answer = min(answer, total_cost)

    return answer