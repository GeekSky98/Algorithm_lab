from collections import deque

n, m = map(int, input().split())
data = [list(map(int, input().split())) for i in range(n)]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

ice_list = deque()
ice_amt = 0
for i in range(n):
    for j in range(m):
        target = data[i][j]
        if target != 0:
            ice_list.append((i,j,target))
            ice_amt += 1

def melt():
    global ice_amt
    melt_list = []
    for _ in range(ice_amt):
        i, j, a = ice_list.popleft()
        for dx, dy in directions:
            if 0 <= i + dx < n and 0 <= j + dy < m and data[i + dx][j + dy] == 0:
                a -= 1
        if a > 0:
            data[i][j] = a
            ice_list.append((i,j,a))
        else:
            melt_list.append((i,j))
            ice_amt -= 1
    for x, y in melt_list:
        data[x][y] = 0

def bfs():
    visit_set = set()
    s_x, s_y = ice_list[0][0], ice_list[0][1]
    queue = deque([(s_x, s_y)])
    visit_set.add((s_x, s_y))
    cnt = 0
    while queue:
        x, y = queue.popleft()
        cnt += 1

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and data[nx][ny] != 0 and (nx, ny) not in visit_set:
                visit_set.add((nx, ny))
                queue.append((nx, ny))

    return False if cnt == ice_amt else True

def solution():
    year = 0
    while True:
        melt()
        year += 1
        if ice_amt == 0:
            return 0
        if bfs():
            return year

print(solution())