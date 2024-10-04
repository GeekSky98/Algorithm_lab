import sys
from collections import deque

arr = [list(list(sys.stdin.readline().strip())) for i in range(12)]
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def detect_4(arr):
    puyo_flag = False
    for i in range(12):
        for j in range(6):
            if arr[i][j] != ".":
                target = arr[i][j]
                queue = deque([(i, j)])
                target_list = set()
                while queue:
                    x, y = queue.popleft()
                    target_list.add((x, y))
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < 12 and 0 <= ny < 6 and arr[nx][ny] == target and (nx, ny) not in target_list:
                            queue.append((nx, ny))
                if len(target_list) >= 4:
                    for x, y in target_list:
                        arr[x][y] = "."
                    puyo_flag = True
    return puyo_flag

def refresh(arr):
    for i in range(6):
        stop_flag = False
        for j in range(11, -1, -1):
            if stop_flag:
                break
            if arr[j][i] == ".":
                for u in range(j-1, -1, -1):
                    if arr[u][i] != ".":
                        arr[j][i] = arr[u][i]
                        arr[u][i] = "."
                        break
                    if u == 0:
                        stop_flag = True

puyo_cnt = 0
while True:
    if not detect_4(arr):
        break
    puyo_cnt += 1
    refresh(arr)

print(puyo_cnt)