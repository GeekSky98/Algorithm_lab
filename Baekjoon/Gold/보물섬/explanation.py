import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().strip()) for _ in range(n)]

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(start_x, start_y, limit_x, limit_y, grid):
    queue = deque([(start_x, start_y, 0)])
    visited = [[0] * m for _ in range(n)]
    visited[start_x][start_y] = 1
    max_value = 0

    while queue:
        x, y, cost = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < limit_x and 0 <= ny < limit_y and visited[nx][ny] == 0 and grid[nx][ny] == "L":
                queue.append((nx, ny, cost + 1))
                visited[nx][ny] = 1
                max_value = max(max_value, cost + 1)

    return max_value

max_dist = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == "L":
            max_dist = max(max_dist, bfs(i, j, n, m, arr))

print(max_dist)