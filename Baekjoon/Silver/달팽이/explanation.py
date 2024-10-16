n = int(input())
target = int(input())

arr = [[0] * n for _ in range(n)]

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
d_idx = 0

num = n * n
x = y = 0
answer = []
while num > 0:
    arr[x][y] = num
    if num == target:
        answer = [x+1, y+1]
    num -= 1

    dx, dy = directions[d_idx % len(directions)]
    nx, ny = x + dx, y + dy
    if nx < 0 or nx >=n or ny <0 or ny >=n or arr[nx][ny] != 0:
        d_idx += 1
        dx, dy = directions[d_idx % len(directions)]
        x, y = x + dx, y + dy
    else:
        x, y = nx, ny

for i in range(n):
    print(" ".join(map(str, arr[i])))
print(" ".join(map(str, answer)))