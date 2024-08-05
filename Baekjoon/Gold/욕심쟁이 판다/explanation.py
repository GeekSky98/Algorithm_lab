import sys
from collections import deque
sys.setrecursionlimit(100000)

n = int(input())
forest = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

dp = [[-1] * n for _ in range(n)]

def dfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 1

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and forest[nx][ny] > forest[x][y]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)

    return dp[x][y]


max_move = 0
for i in range(n):
    for j in range(n):
        max_move = max(max_move, dfs(i, j))

print(max_move)