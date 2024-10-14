from heapq import heappush, heappop
from collections import defaultdict


def solution(n, paths, gates, summits):
    graph = defaultdict(list)
    for s, e, c in paths:
        graph[s].append((e, c))
        graph[e].append((s, c))

    dist = [float('inf')] * (n + 1)
    summits_set = set(summits)
    queue = []
    for g in gates:
        heappush(queue, (0, g))
        dist[g] = 0

    while queue:
        inten, node = heappop(queue)

        if inten > dist[node]:
            continue

        if node in summits_set:
            continue

        for next_node, cost in graph[node]:
            new_cost = max(cost, inten)
            if new_cost < dist[next_node]:
                heappush(queue, (new_cost, next_node))
                dist[next_node] = new_cost

    answer = [-1, float('inf')]
    for s in sorted(summits):
        min_value = dist[s]
        if min_value < answer[1]:
            answer = [s, min_value]

    return answer