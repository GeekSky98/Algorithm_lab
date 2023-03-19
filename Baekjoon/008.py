# https://www.acmicpc.net/problem/9084

import sys

input = int(sys.stdin.readline())
result = ""

for t in range(input):
    N = int(sys.stdin.readline())
    coin = list(map(int, sys.stdin.readline().split(' ')))
    M = int(sys.stdin.readline())
    dp = [0] * (M + 1)

    for n in range(N):
        dis = coin[n]
        if (dis > M):
            continue
        dp[dis] += 1

        for i in range(dis + 1, M + 1):
            dp[i] += dp[i - dis]

    result += str(dp[M]) + "\n"

print(result)