import sys

N = int(sys.stdin.readline())
ARR = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

def solution(n, arr):
    dp = [0] * (n+1)

    for i, (day, revenue) in enumerate(arr):
        if i + day <= n:
            dp[i + day] = max(dp[i + day], dp[i] + revenue)
        dp[i+1] = max(dp[i+1], dp[i])

    return dp[-1]

print(solution(N, ARR))