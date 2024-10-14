from collections import deque


def solution(maps):
    answer = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    max_x, max_y = len(maps), len(maps[0])
    visited = [[False] * max_y for _ in range(max_x)]

    def bfs(x, y):
        queue = deque([(x, y)])
        visited[x][y] = True
        max_size = 0
        while queue:
            x, y = queue.popleft()

            max_size += int(maps[x][y])

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < max_x and 0 <= ny < max_y and not visited[nx][ny] and maps[nx][ny] != 'X':
                    visited[nx][ny] = True
                    queue.append((nx, ny))

        return max_size

    for i in range(max_x):
        for j in range(max_y):
            if not visited[i][j] and maps[i][j] != 'X':
                answer.append(bfs(i, j))

    return sorted(answer) if answer else [-1]

print(solution(["X591X","X1X5X","X231X", "1XXX1"]))