import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
cheese = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def air_detect(arr, n, m):
    queue = deque([(0, 0)])
    out_air = [[0] * m for _ in range(n)]

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not out_air[nx][ny] and arr[nx][ny] != 1:
                out_air[nx][ny] = 1
                queue.append((nx, ny))

    return out_air

cnt = 0
while True:
    out_air_arr = air_detect(cheese, n, m)
    del_cnt = 0
    for i in range(n):
        for j in range(m):
            if cheese[i][j] == 1:
                if sum(1 for x, y in directions if 0 <= i+x < n and 0 <= j+y < m and out_air_arr[i+x][j+y]) >= 2:
                    cheese[i][j] = 0
                    del_cnt += 1
    if del_cnt == 0:
        break
    cnt += 1

print(cnt)