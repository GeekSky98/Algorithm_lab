import sys
sys.setrecursionlimit(10 ** 8)

n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

dp = [[-1] * m for i in range(n)]

def dfs(x, y):
    if (x, y) == (n - 1, m - 1):
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and arr[x][y] > arr[nx][ny]:
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]

print(dfs(0, 0))