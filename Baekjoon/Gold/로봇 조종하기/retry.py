n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]

dp = [[-float('inf')]*m for _ in range(n)]
dp[0][0] = arr[0][0]
for i in range(1, m):
    dp[0][i] =dp[0][i-1] + arr[0][i]

for i in range(1, n):

    left = [-float('inf')] * m
    left[0] = dp[i-1][0] + arr[i][0]
    for l in range(1, m):
        left[l] = max(dp[i-1][l], left[l-1]) + arr[i][l]

    right = [-float('inf')] * m
    right[-1] = dp[i-1][-1] + arr[i][-1]
    for r in range(m-2, -1, -1):
        right[r] = max(dp[i-1][r], right[r+1]) + arr[i][r]

    for j in range(m):
        dp[i][j] = max(left[j], right[j])

print(dp[-1][-1])
