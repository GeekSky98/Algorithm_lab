import sys

n, m = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().strip()) for i in range(n)]

def dfs(x, y):
    global safe_cnt
    visited[x][y] = True
    path[x][y] = True

    if arr[x][y] == 'U':
        nx, ny = x - 1, y
    elif arr[x][y] == 'D':
        nx, ny = x + 1, y
    elif arr[x][y] == 'L':
        nx, ny = x, y - 1
    else:
        nx, ny = x, y + 1

    if not visited[nx][ny]:
        dfs(nx, ny)
    elif path[nx][ny]:
        safe_cnt += 1

    path[x][y] = False

visited = [[False] * m for _ in range(n)]
path = [[False] * m for _ in range(n)]
safe_cnt = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            dfs(i, j)

print(safe_cnt)