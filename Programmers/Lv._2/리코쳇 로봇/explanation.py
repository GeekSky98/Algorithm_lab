from heapq import heappop, heappush
def solution(board):
    answer = 0
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
    board = [list(row) for row in board]
    row_len, col_len = len(board), len(board[0])
    for i in range(row_len):
        for j in range(col_len):
            if board[i][j] == "R":
                row, col = i, j
                break
    visited = [[False] * col_len for _ in range(row_len)]
    queue = [(0, row, col)]
    visited[row][col] = True

    while queue:
        cnt, x, y = heappop(queue)

        if board[x][y] == "G":
            return cnt

        for nx, ny in direction:
            dx, dy = x, y
            while 0 <= dx + nx < row_len and 0 <= dy + ny < col_len and board[dx+nx][dy+ny] != "D":
                dx += nx
                dy += ny
            if not visited[dx][dy]:
                visited[dx][dy] = True
                heappush(queue, (cnt + 1, dx, dy))

    return -1