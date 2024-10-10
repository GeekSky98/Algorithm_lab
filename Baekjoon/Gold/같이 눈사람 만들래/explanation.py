import sys
from itertools import combinations

n = int(input())
data = list(map(int, input().split()))

pairs = []
for i, j in combinations(range(n), 2):
    pairs.append((data[i]+data[j], i, j))

pairs.sort()
min_cost = float('inf')
for i in range(len(pairs)-1):
    h, x, y = pairs[i]
    h2, x2, y2 = pairs[i+1]

    if len({x, y, x2, y2}) == 4:
        min_cost = min(min_cost, abs(h-h2))

    if min_cost == 0:
        break

print(min_cost)