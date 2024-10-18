from collections import deque

def solution(maps):
    x_len, y_len = len(maps), len(maps[0])

    queue = deque([(0, 0, 1)])
    visited = [[False] * y_len for _ in range(x_len)]
    visited[0][0] = True

    while queue:
        x, y, c = queue.popleft()

        if (x, y) == (x_len - 1, y_len - 1):
            return c

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < x_len and 0 <= ny < y_len and not visited[nx][ny] and maps[nx][ny] == 1:
                queue.append((nx, ny, c + 1))
                visited[nx][ny] = True

    return -1