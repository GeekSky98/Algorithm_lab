import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

dp = arr.copy()

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+arr[i])

print(max(dp))
