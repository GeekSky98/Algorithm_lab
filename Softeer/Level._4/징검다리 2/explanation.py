import sys
from bisect import bisect_left

n = int(sys.stdin.readline().strip())
stone = list(map(int, sys.stdin.readline().split()))

def detect(N, arr):
    dp = []
    left_bi = [0] * N
    for i, val in enumerate(arr):
        pos = bisect_left(dp, val)
        if pos == len(dp):
            dp.append(val)
        else:
            dp[pos] = val
        left_bi[i] = pos + 1
    return left_bi

front_dp = detect(n, stone)
back_dp = detect(n, stone[::-1])[::-1]

max_stone = 0
for i in range(n):
    max_stone = max(max_stone, front_dp[i]+back_dp[i]-1)

print(max_stone)