import sys
from collections import defaultdict
from heapq import heappush, heappop

n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

degree = [0] * (n + 1)
graph = defaultdict(list)

for u, d in arr:
    graph[u].append(d)
    degree[d] += 1

queue = []
for i in range(1, n+1):
    if degree[i] == 0:
        heappush(queue, i)

result = []
while queue:
    current = heappop(queue)
    result.append(current)

    for next in graph[current]:
        degree[next] -= 1
        if degree[next] == 0:
            heappush(queue, next)

print(" ".join(map(str, result)))