import sys
from heapq import heappush, heappop
node, line = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph_list = [list(map(int, sys.stdin.readline().split())) for _ in range(line)]

dp = [float('inf')] * (node + 1)
graph = [[] for _ in range(node+1)]
for g in graph_list:
    graph[g[0]].append((g[1], g[2]))

dp[start] = 0
heap = [(0, start)]

while heap:
    cost, target = heappop(heap)

    if dp[target] < cost:
        continue
    else:
        for next, weight in graph[target]:
            next_cost = cost + weight
            if next_cost < dp[next]:
                dp[next] = next_cost
                heappush(heap, (next_cost, next))

for i in range(1, node + 1):
    if dp[i] == float('inf'):
        print("INF")
    else:
        print(dp[i])