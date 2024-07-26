import sys

c, n = map(int, sys.stdin.readline().split())
ways = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

def solution(c, n, ways):
    dp = [float('inf')] * (c+101)
    dp[0] = 0

    for cost, customer in ways:
        for i in range(1, c+101):
            dp[i] = min(dp[i], dp[i-customer]+cost)

    return min(dp[c:])

print(solution(c, n, ways))
