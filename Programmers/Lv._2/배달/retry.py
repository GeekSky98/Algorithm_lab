from collections import defaultdict
from heapq import heappop, heappush

def solution(N, road, K):
    graph = defaultdict(list)
    for s, e, c in road:
        graph[s].append((e, c))
        graph[e].append((s, c))

    queue = []
    heappush(queue, (0, 1))
    dist = [float('inf')] * (N + 1)
    dist[1] = 0

    while queue:
        cost, node = heappop(queue)

        if cost > dist[node]:
            continue

        for next_node, next_cost in graph[node]:
            new_cost = cost + next_cost
            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                heappush(queue, (new_cost, next_node))

    return sum(1 if i <= K else 0 for i in dist)
