import sys
from collections import deque

N = int(sys.stdin.readline())

def solution(n):
    queue = deque([(0, n)])
    while queue:
        cnt, num = queue.popleft()
        if num == 1:
            return cnt

        if num % 3 == 0:
            queue.append((cnt + 1, num // 3))
        if num % 2 == 0:
            queue.append((cnt + 1, num // 2))
        queue.append((cnt+1, num-1))

print(solution(N))
