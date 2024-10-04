import sys
from collections import defaultdict
from heapq import heappush, heappop

n = int(input())
m = int(input())
bus = [tuple(map(int, input().split())) for i in range(m)]
start, target = map(int, input().split())

graph = defaultdict(list)
for s, e, c in bus:
    graph[s].append((c, e))

queue = [(0, start)]
dist = [float('inf')] * (n + 1)
dist[start] = 0

while queue:
    c, s = heappop(queue)

    if s == target:
        print(c)
        break

    if c > dist[s]:
        continue

    for cost, node in graph[s]:
        new_cost = cost + c
        if new_cost < dist[node]:
            dist[node] = new_cost
            heappush(queue, (new_cost, node))