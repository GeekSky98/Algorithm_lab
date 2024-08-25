import sys
n, k = map(int, sys.stdin.readline().split())
money = list(set(int(sys.stdin.readline().strip()) for _ in range(n)))

dp = [float('inf')] * (k+1)
dp[0] = 0

for m in money:
    for i in range(m, k+1):
        dp[i] = min(dp[i], dp[i-m]+1)

print(-1 if dp[-1] == float('inf') else dp[-1])