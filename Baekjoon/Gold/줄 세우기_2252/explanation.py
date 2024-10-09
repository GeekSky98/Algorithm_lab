import sys
from collections import deque, defaultdict

n, m = map(int, sys.stdin.readline().split())
heights = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

degree = [0] * (n + 1)
graph = defaultdict(list)
for a, b in heights:
    graph[a].append(b)
    degree[b] += 1

queue = deque()
for i in range(1, n + 1):
    if degree[i] == 0:
        queue.append(i)

result = []
while queue:
    current = queue.popleft()
    result.append(current)

    for i in graph[current]:
        degree[i] -= 1
        if degree[i] == 0:
            queue.append(i)

print(" ".join(map(str, result)))