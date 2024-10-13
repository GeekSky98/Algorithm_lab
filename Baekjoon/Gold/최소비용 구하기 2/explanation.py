import sys
from collections import defaultdict
from heapq import heappush, heappop

n = int(input())
m = int(input())
bus = [tuple(map(int, input().split())) for i in range(m)]
start, target = map(int, input().split())

graph = defaultdict(list)
for a, b, c in bus:
    graph[a].append((b, c))

dist = [float('inf')] * (n + 1)
parent = [-1] * (n + 1)
dist[start] = 0
queue = [(0, start)]

while queue:
    cost, node = heappop(queue)

    if cost > dist[node]:
        continue

    if node == target:
        break

    for next_node, next_cost in graph[node]:
        if next_cost + cost < dist[next_node]:
            dist[next_node] = next_cost + cost
            parent[next_node] = node
            heappush(queue, (next_cost+cost, next_node))

path = []
p = target
while p != -1:
    path.append(p)
    p = parent[p]

print(dist[target])
print(len(path))
print(" ".join(map(str, reversed(path))))