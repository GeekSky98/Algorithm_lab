import sys
from bisect import bisect_left

n = int(input())
data = list(map(int, input().split()))

dp = []
for i in data:
    pos = bisect_left(dp, i)
    if pos == len(dp):
        dp.append(i)
    else:
        dp[pos] = i

print(len(dp))