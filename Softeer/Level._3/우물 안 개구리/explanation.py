import sys
from collections import defaultdict

n, m = map(int, sys.stdin.readline().split())
weight = list(map(int, sys.stdin.readline().split()))
edge = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]

graph = defaultdict(list)
for i, j in edge:
    graph[i].append(j)
    graph[j].append(i)

cnt = 0
for i in range(1, n+1):
    im_strong = True
    me = weight[i-1]
    for f in graph[i]:
        if weight[f-1] >= me:
            im_strong = False
            break
    if im_strong:
        cnt += 1

print(cnt)