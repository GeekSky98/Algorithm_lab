from heapq import heappush, heappop
from collections import defaultdict

def solution(n, costs):
    graph = defaultdict(list)
    for s, e, c in costs:
        graph[s].append((c, e))
        graph[e].append((c, s))

    queue = [(0, 0)]
    visited = [False] * n
    total_cost = 0
    while queue:
        cost, node = heappop(queue)

        if visited[node]:
            continue

        visited[node] = True
        total_cost += cost

        for next_cost, next_node in graph[node]:
            if not visited[next_node]:
                heappush(queue, (next_cost, next_node))

    return total_cost


print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))