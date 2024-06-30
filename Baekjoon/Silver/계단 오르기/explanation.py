import sys
n = int(sys.stdin.readline())
stair = [int(sys.stdin.readline()) for _ in range(n)]

def solution(n, stair):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return sum(stair)

    dp = [0] * n
    dp[0] = stair[0]
    dp[1] = dp[0] + stair[1]
    dp[2] = max(dp[0] + stair[2], stair[1] + stair[2])

    for i in range(3, n):
        dp[i] = max(dp[i-2] + stair[i], dp[i-3] + stair[i-1] + stair[i])

    return dp[-1]

print(solution(n, stair))