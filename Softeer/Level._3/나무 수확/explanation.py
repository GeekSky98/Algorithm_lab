import sys
from collections import deque

n = int(sys.stdin.readline().strip())
farm = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

answer = 0

direction = [(1, 0), (0, 1)]
queue = deque([(farm[0][0], farm[0][0], 0, 0)])

while queue:
    got, max_value, x, y = queue.popleft()

    if (x, y) == (n-1, n-1):
        answer = max(answer, got + max_value)

    for dx, dy in direction:
        nx, ny = x+dx, y+dy
        if nx < n and ny < n:
            next_num = farm[nx][ny]
            queue.append((got + next_num, max(max_value, next_num), nx, ny))

print(answer)