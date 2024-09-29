import sys
from itertools import combinations
from collections import deque
from copy import deepcopy

n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

zone_0 = []
zone_1 = []
zone_2 = []

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            zone_0.append((i, j))
        elif arr[i][j] == 1:
            zone_1.append((i, j))
        else:
            zone_2.append((i, j))

barrier_combi = list(combinations(zone_0, 3))

def safety_cnt(arr):
    return sum(a.count(0) for a in arr)

def virus(arr_copy):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque(zone_2)

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and arr_copy[nx][ny] == 0:
                arr_copy[nx][ny] = 2
                queue.append((nx, ny))

    return safety_cnt(arr_copy)

max_safety = 0
for combi in barrier_combi:
    temp_arr = deepcopy(arr)
    for x, y in combi:
        temp_arr[x][y] = 1

    max_safety = max(max_safety, virus(temp_arr))

print(max_safety)