import sys
from bisect import bisect_left

n = int(input())
data = list(map(int, input().split()))

dp = []
dp_idx = []

for i in data:
    pos = bisect_left(dp, i)
    if pos == len(dp):
        dp.append(i)
    else:
        dp[pos] = i
    dp_idx.append(pos)

dp_length = len(dp) - 1
answer = []
for i in range(n-1, -1, -1):
    if dp_idx[i] == dp_length:
        answer.append(data[i])
        dp_length -= 1

print(len(answer))
print(" ".join(map(str, sorted(answer))))