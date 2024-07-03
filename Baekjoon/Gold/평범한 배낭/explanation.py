import sys

n, k = map(int, sys.stdin.readline().split())
items = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

def solution(n, k, items):
    dp = [0] * (k+1)

    for weight, price in items:
        for i in range(k, weight-1, -1):
            dp[i] = max(dp[i], dp[i-weight] + price)

    return dp[k]

print(solution(n,k,items))