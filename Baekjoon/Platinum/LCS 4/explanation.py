import sys
from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

b_index = [0] * (n+1)
for i in range(n):
    b_index[b[i]] = i
lis = [b_index[i] for i in a]

dp = []
for i in lis:
    pos = bisect_left(dp, i)
    if pos < len(dp):
        dp[pos] = i
    else:
        dp.append(i)

print(len(dp))