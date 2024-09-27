import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
s, x, y = map(int, sys.stdin.readline().split())

def solution(n, k, arr, s, x, y):
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                queue.append((arr[i][j], i, j))
    queue = deque(sorted(queue, key=lambda x: x[0]))

    for _ in range(s):
        for _ in range(len(queue)):
            num, row, col = queue.popleft()
            for dx, dy in direction:
                nx, ny = row + dx, col + dy
                if 0 <= nx < n and 0 <= ny < n and not arr[nx][ny]:
                    arr[nx][ny] = num
                    queue.append((num, nx, ny))

    return arr[x-1][y-1] if arr[x-1][y-1] else 0

print(solution(n, k, arr, s, x, y))