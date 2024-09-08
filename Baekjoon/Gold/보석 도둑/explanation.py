import sys
from heapq import heappop, heappush

n, k = map(int, sys.stdin.readline().split())
j = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(n)], key=lambda x: x[0])
bag = sorted([int(sys.stdin.readline().strip()) for _ in range(k)])

total = j_idx = 0
queue = []
for b in bag:
    while j_idx < n and j[j_idx][0] <= b:
        heappush(queue, -j[j_idx][1])
        j_idx += 1
    if queue:
        total += (heappop(queue)) * -1

print(total)