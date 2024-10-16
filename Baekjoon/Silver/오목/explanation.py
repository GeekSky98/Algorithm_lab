import sys
from collections import deque

data = sys.stdin.read()
board = [list(map(int, line.split())) for line in data.splitlines()]
b_len = len(board)
directions = [(1, 0), (0, 1), (1, 1), (1, -1)]

def detect(x, y, c):
    queue = deque()
    for i in range(4):
        queue.append((x,y,1,i))
    max_cnt = 1
    dir_3_check = None
    while queue:
        x, y, cost, direction = queue.popleft()

        max_cnt = max(max_cnt, cost)
        if direction == 3 and cost == 5:
            dir_3_check = (x, y)

        dx, dy = directions[direction]
        nx, ny = x + dx, y + dy
        if 0 <= nx < b_len and 0 <= ny < b_len and board[nx][ny] == c:
            queue.append((nx, ny, cost + 1, direction))

    if max_cnt == 5:
        if dir_3_check:
            return True, dir_3_check
        else:
            return True, False
    else:
        return False, False

def solution():
    for i in range(b_len):
        for j in range(b_len):
            target = board[i][j]
            if target == 1 or target == 2:
                flag, flag_3 = detect(i, j, target)
                if flag:
                    print(target)
                    if flag_3:
                        print(flag_3[0]+1, flag_3[1]+1)
                    else:
                        print(i+1, j+1)
                    return
    print(0)

solution()