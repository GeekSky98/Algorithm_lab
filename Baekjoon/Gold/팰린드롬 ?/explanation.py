import sys
n = int(input())
nums = list(map(int, sys.stdin.readline().split()))
m = int(input())
questions = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]

dp = [[0] * n for _ in range(n)]
for i in range(n):
    dp[i][i] = 1

for i in range(n - 1):
    if nums[i] == nums[i + 1]:
        dp[i][i+1] = 1

for length in range(2, n):
    for i in range(n - length):
        j = i + length
        if nums[i] == nums[j] and dp[i+1][j-1] == 1:
            dp[i][j] = 1

for s, e in questions:
    print(dp[s-1][e-1])