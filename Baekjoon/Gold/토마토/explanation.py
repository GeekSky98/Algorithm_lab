import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def solution(m, n, arr):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[0] * m for _ in range(n)]
    queue = deque()
    tomato = [(i, j) for i in range(n) for j in range(m) if arr[i][j] == 1]
    for x, y in tomato:
        queue.append((x, y, 0))
        visited[x][y] = 1

    last_day = 0
    while queue:
        x, y, day = queue.popleft()
        last_day = day

        for dy, dx in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                queue.append((nx, ny, day + 1))
                arr[nx][ny] = 1
                visited[nx][ny] = 1


    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                return -1

    return last_day

print(solution(m, n, arr))