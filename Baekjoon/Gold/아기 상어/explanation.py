import sys
from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def find_shark():
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 9:
                arr[i][j] = 0
                return i, j

def bfs(x, y, size):
    visited = [[False] * n for _ in range(n)]
    queue = deque([(x, y, 0)])
    visited[x][y] = True
    fish = []
    max_dist = float('inf')

    while queue:
        x, y, cost = queue.popleft()

        if 0 < arr[x][y] < size:
            if cost <= max_dist:
                fish.append((x, y))
                max_dist = cost
            else:
                break

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] <= size:
                queue.append((nx, ny, cost + 1))
                visited[nx][ny] = True

    if fish:
        fish.sort()
        x, y = fish[0][0], fish[0][1]
        arr[x][y] = 0
        return x, y, max_dist
    else:
        return -1, -1, -1

answer = 0
shark_size = 2
fish_cnt = 0
s_x, s_y = find_shark()
while True:
    s_x, s_y, cost = bfs(s_x, s_y, shark_size)
    if s_x == -1:
        break
    answer += cost
    fish_cnt += 1
    if fish_cnt == shark_size:
        shark_size += 1
        fish_cnt = 0

print(answer)