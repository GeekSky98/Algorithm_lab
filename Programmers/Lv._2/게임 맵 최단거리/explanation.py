from collections import deque

def solution(maps):
    h, w = len(maps), len(maps[0])
    visited = [[False for _ in range(w)] for _ in range(h)]
    queue = deque([(0, 0, 1)])

    while queue:
        y, x, dist = queue.popleft()

        if y == h - 1 and x == w - 1:
            return dist

        for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny, nx = y+j, x+i
            if 0 <= ny < h and 0 <= nx < w and maps[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((ny, nx, dist+1))

    return -1