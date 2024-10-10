import sys
from collections import defaultdict
from heapq import heappush, heappop

n, e = map(int, sys.stdin.readline().split())
edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(e)]
middle = list(map(int, sys.stdin.readline().split()))

graph = defaultdict(list)
for a, b, c in edges:
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(graph, start, end):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    visited = [False] * (n + 1)
    queue = [(0, start)]

    while queue:
        cost, node = heappop(queue)

        if node == end:
            return cost

        if visited[node]:
            continue

        visited[node] = True

        for next_node, next_cost in graph[node]:
            if not visited[next_node]:
                new_dist = cost + next_cost
                if new_dist < dist[next_node]:
                    dist[next_node] = new_dist
                    heappush(queue, (new_dist, next_node))

    return -1 if dist[end] == float('inf') else dist[end]

def solution():
    route = [1] + middle + [n]
    min_cost = float('inf')
    for _ in range(2):
        current_sum = 0
        for i in range(3):
            r = dijkstra(graph, route[i], route[i + 1])
            if r == -1:
                return -1
            current_sum += r
        min_cost = min(min_cost, current_sum)
        route = [1] + list(reversed(middle)) + [n]

    return min_cost

print(solution())
