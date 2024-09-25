import sys

n, k = map(int, sys.stdin.readline().split())
MOD = 1000000000
dp = [[1] + ([0] * n) for _ in range(k + 1)]

for i in range(1, k + 1):
    for j in range(1, n + 1):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD

print(dp[-1][-1])