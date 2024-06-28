import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
car_map = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
point = [tuple(map(lambda x: int(x) - 1, sys.stdin.readline().split())) for _ in range(m)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(x, y, point_idx, visited):
    if point_idx == m:
        return 1

    next_x, next_y = point[point_idx]
    if (x, y) == (next_x, next_y):
        return dfs(next_x, next_y, point_idx + 1, visited)

    path_cnt = 0
    visited[x][y] = True

    for px, py in directions:
        nx, ny = x + px, y + py
        if 0 <= nx < n and 0 <= ny < n and car_map[nx][ny] != 1 and not visited[nx][ny]:
            path_cnt += dfs(nx, ny, point_idx, visited)

    visited[x][y] = False

    return path_cnt


start_x, start_y = point[0]
visited = [[False] * n for _ in range(n)]
result = dfs(start_x, start_y, 1, visited)
print(result)