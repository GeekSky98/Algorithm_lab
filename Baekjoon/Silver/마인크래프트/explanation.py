import sys

n, m, b = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

min_cost = float('inf')
max_height = -1
for h in range(257):
    cost = 0
    used_block = 0
    for i in range(n):
        for j in range(m):
            target = arr[i][j]
            if target > h:
                cost += (target - h) * 2
                used_block -= target - h
            elif target < h:
                cost += h - target
                used_block += h - target
    if used_block <= b and cost <= min_cost:
        max_height = h
        min_cost = cost

print(min_cost, max_height)