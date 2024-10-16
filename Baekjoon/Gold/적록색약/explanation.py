from collections import deque, defaultdict

n = int(input())
arr = [list(input().strip()) for _ in range(n)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def solution(n, arr, flag):
    def dfs(x, y, color):
        queue = deque([(x, y)])
        visited[x][y] = True

        while queue:
            x, y = queue.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] in color:
                    queue.append((nx, ny))
                    visited[nx][ny] = True

    cnt = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                color = [arr[i][j]]
                if flag and (color[0] == 'R' or color[0] == 'G'):
                    color = ['R', 'G']
                cnt += 1
                dfs(i, j, color)

    return cnt

print(solution(n, arr, False), solution(n, arr, True))