import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, list(sys.stdin.readline().strip()))) for i in range(n)]

def solution(n, m, arr):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    queue = deque([(0, 0, 0)]) # x, y, cost, crush
    visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1

    while queue:
        x, y, crush = queue.popleft()

        if (x, y) == (n-1, m-1):
            return visited[x][y][crush]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0 and visited[nx][ny][crush] == 0:
                    visited[nx][ny][crush] = visited[x][y][crush] + 1
                    queue.append((nx, ny, crush))

                elif crush == 0 and arr[nx][ny] == 1:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    queue.append((nx, ny, 1))

    return -1

print(solution(n, m, arr))