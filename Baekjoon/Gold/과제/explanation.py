import sys
from heapq import heappop, heappush

n = int(input())
sub = sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(n)], key=lambda x: x[0])

queue = []

for day, cost in sub:
    heappush(queue, cost)

    if len(queue) > day:
        heappop(queue)

print(sum(queue))