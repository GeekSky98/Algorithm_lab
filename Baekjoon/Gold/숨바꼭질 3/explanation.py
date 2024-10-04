import sys
from heapq import heappush, heappop
n, k = map(int, sys.stdin.readline().split())
min_pos, max_pos = 0, 100000

queue = [(0, n)]
visited = [float('inf')] * (max_pos + 1)
visited[n] = 0

while queue:
    c, x = heappop(queue)
    if x == k:
        print(c)
        break

    for i, j in enumerate([x+1, x-1, x*2]):
        if min_pos <= j <= max_pos:
            if i == 2 and visited[j] > c:
                heappush(queue, (c, j))
                visited[j] = c
            elif i in [0, 1] and visited[j] > c + 1:
                heappush(queue, (c+1, j))
                visited[j] = c + 1