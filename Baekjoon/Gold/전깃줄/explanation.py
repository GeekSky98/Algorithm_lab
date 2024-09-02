import sys
from bisect import bisect_left
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n)]
edges.sort(key=lambda x: x[0])

b_line = [i[1] for i in edges]
dp = []
for b in b_line:
    pos = bisect_left(dp, b)
    if pos < len(dp):
        dp[pos] = b
    else:
        dp.append(b)

print(n - len(dp))