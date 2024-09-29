import sys

r, c = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().strip()) for _ in range(r)]
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

visited = [False] * 26
max_length = 1
def dfs(x, y, cnt):
    global max_length
    max_length = max(max_length, cnt)
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c and not visited[ord(arr[nx][ny]) - ord("A")]:
            visited[ord(arr[nx][ny]) - ord("A")] = True
            dfs(nx, ny, cnt + 1)
            visited[ord(arr[nx][ny]) - ord("A")] = False

dfs(0, 0, 1)
print(max_length)




