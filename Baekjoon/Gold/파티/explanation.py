import sys
from heapq import heappop, heappush
from collections import defaultdict
n, m, x = map(int, sys.stdin.readline().split())
edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]

graph = defaultdict(list)
graph_reverse = defaultdict(list)
for start, end, cost in edges:
    graph[start].append((end, cost))
    graph_reverse[end].append((start, cost))

def dijkstra(s, g, n):
    dist = [float('inf')] * (n + 1)
    dist[s] = 0
    queue = [(0, s)]

    while queue:
        now_cost, now_node = heappop(queue)

        if now_cost > dist[now_node]:
            continue

        for next_node, next_cost in g[now_node]:
            new_cost = next_cost + now_cost
            if new_cost < dist[next_node]:
                heappush(queue, (new_cost, next_node))
                dist[next_node] = new_cost

    return dist

front_cost = dijkstra(x, graph, n)
back_cost = dijkstra(x, graph_reverse, n)

max_dist = 0
for i in range(1, n+1):
    total_dist = front_cost[i] + back_cost[i]
    max_dist = max(max_dist, total_dist)

print(max_dist)