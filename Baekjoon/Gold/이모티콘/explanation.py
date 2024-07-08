import sys
from collections import deque

N = int(sys.stdin.readline())

def solution(n):
    queue = deque([(1, 0, 0)])  # 이모티콘 수, 클립보드 이모티콘 수
    visited = set((1,0))

    while queue:
        e_num, clip, time = queue.popleft()
        if e_num == n:
            return time

        if (e_num, e_num) not in visited:
            visited.add((e_num, e_num))
            queue.append((e_num, e_num, time + 1))

        if clip > 0 and (e_num + clip, clip) not in visited:
            visited.add((e_num + clip, clip))
            queue.append((e_num + clip, clip, time + 1))

        if e_num > 0 and (e_num - 1, clip) not in visited:
            visited.add((e_num - 1, clip))
            queue.append((e_num - 1, clip, time + 1))

print(solution(N))