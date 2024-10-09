import sys
from bisect import bisect_left

n = int(input())
edges = sorted(tuple(map(int, input().split())) for _ in range(n))

dp = []
lis_idx = []
for edge in [i[1] for i in edges]:
    pos = bisect_left(dp, edge)
    if pos == len(dp):
        dp.append(edge)
    else:
        dp[pos] = edge
    lis_idx.append(pos)

length = len(dp) - 1
lis_path = set()
for i in range(n - 1, -1, -1):
    if lis_idx[i] == length:
        lis_path.add(i)
        length -= 1

answer = []
for i in range(n):
    if i not in lis_path:
        answer.append(edges[i][0])
answer.sort()

print(len(answer))
for i in answer:
    print(i)