from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    arr = [[-1] * 102 for _ in range(102)]  # 1칸 짜리 벽 통과 방지 * 2
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if arr[i][j] != -2:
                    if i == x1 or i == x2 or j == y1 or j == y2:
                        arr[i][j] = 0
                    else:
                        arr[i][j] = -2

    characterX, characterY = characterX * 2, characterY * 2
    itemX, itemY = itemX * 2, itemY * 2

    queue = deque([(characterX, characterY, 0)])
    arr[characterX][characterY] = 1

    while queue:
        x, y, c = queue.popleft()

        if x == itemX and y == itemY:
            return c // 2

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 102 and 0 <= ny < 102 and arr[nx][ny] == 0:
                queue.append((nx, ny, c + 1))
                arr[nx][ny] = 1

    return answer