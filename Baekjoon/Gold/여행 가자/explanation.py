import sys
from collections import defaultdict, deque
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
plan = list(map(int, sys.stdin.readline().split()))

graph = defaultdict(list)
for i, possible in enumerate(edges):
    for j, p in enumerate(possible):
        if p:
            graph[i+1].append(j+1)

group_list = [0] * (n+1)
for i in range(1, n+1):
    if group_list[i]:
        continue

    queue = deque([i])
    while queue:
        current_city = queue.popleft()
        group_list[current_city] = i

        for next_city in graph[current_city]:
            if not group_list[next_city]:
                queue.append(next_city)

group = group_list[plan[0]]
print("YES" if all([group_list[p] == group for p in plan]) else "NO")