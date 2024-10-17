import sys
from heapq import heappush, heappop
queue = []
for _ in range(int(sys.stdin.readline())):
    v = int(sys.stdin.readline())
    if v == 0:
        if queue: print(-heappop(queue))
        else: print(0)
    else: heappush(queue, -v)


# -------- 입력 효율 증대 버전
import sys
from heapq import heappush, heappop

input = sys.stdin.readline
queue = []
result = []

for _ in range(int(input())):
    v = int(input())
    if v == 0:
        if queue:
            result.append(-heappop(queue))
        else:
            result.append(0)
    else:
        heappush(queue, -v)

sys.stdout.write("\n".join(map(str, result)) + "\n")
