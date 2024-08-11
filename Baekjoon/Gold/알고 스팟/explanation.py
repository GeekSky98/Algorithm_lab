import sys
from heapq import heappop, heappush

n, m = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(m)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
queue = [(0, 0, 0)]

visited = [[False] * n for _ in range(m)]

while queue:
    cost, x, y = heappop(queue)

    if visited[x][y]:
        continue
    visited[x][y] = True

    if (x, y) == (m-1, n-1):
        print(cost)
        break

    for px, py in directions:
        nx, ny = x + px, y + py
        if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
            heappush(queue, (cost + maze[nx][ny], nx, ny))