import sys
from heapq import heappush, heappop
queue = []
for _ in range(int(sys.stdin.readline())):
    v = int(sys.stdin.readline())
    if v == 0:
        if queue: print(heappop(queue))
        else: print(0)
    else: heappush(queue, v)