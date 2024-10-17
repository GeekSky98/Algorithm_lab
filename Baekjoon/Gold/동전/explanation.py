n, k = map(int, input().split())
money = [int(input()) for _ in range(n)]

dp = [float('inf')] * (k + 1)
dp[0] = 0
for i in money:
    for j in range(i, k + 1):
        dp[j] = min(dp[j-i] + 1, dp[j])

print(dp[k])

# ================= 갯수를 구하는 문제였다.

n, k = map(int, input().split())
money = [int(input()) for _ in range(n)]
dp = [0] * (k + 1)
dp[0] = 1

for i in money:
    for j in range(i, k+1):
        dp[j] += dp[j-i]

print(dp[k])