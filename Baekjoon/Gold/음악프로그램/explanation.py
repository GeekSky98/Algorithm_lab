import sys
from collections import defaultdict, deque
n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for i in range(m)]

degree = [0] * (n + 1)
graph = defaultdict(list)
for sub in arr:
    for s in range(1, sub[0]):
        graph[sub[s]].append(sub[s+1])
        degree[sub[s+1]] += 1

queue = deque()
for i in range(1, n+1):
    if degree[i] == 0:
        queue.append(i)

answer = []
while queue:
    num = queue.popleft()
    answer.append(num)

    for sub in graph[num]:
        degree[sub] -= 1
        if degree[sub] == 0:
            queue.append(sub)

if len(answer) == n:
    for i in answer:
        print(i)
else:
    print(0)