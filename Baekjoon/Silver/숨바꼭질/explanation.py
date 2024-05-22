import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())

def solution(me, you):
    if me == you:
        return 0

    max_dist = 100001
    visited = [False] * (max_dist+1)
    queue = deque([(me, 0)])

    while queue:
        m, y = queue.popleft()
        if m == you:
            return y

        for next_num in [m+1, m-1, m*2]:
            if 0 <= next_num < max_dist and not visited[next_num]:
                queue.append((next_num, y+1))
                visited[next_num] = True

print(solution(n, k))