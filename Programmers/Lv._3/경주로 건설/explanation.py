from heapq import heappop, heappush, heapify

def solution(board):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상 하 좌 우
    length = len(board)

    queue = [(0, 0, 0, 1), (0, 0, 0, 3)]
    dist = [[[float('inf')] * 4 for i in range(length)] for _ in range(length)]
    dist[0][0][1] = dist[0][0][3] = 0

    while queue:
        cost, x, y, d = heappop(queue)

        if (x, y) == (length-1, length-1):
            return cost

        if cost > dist[x][y][d]:
            continue

        for i, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            if 0 <= nx < length and 0 <= ny < length and board[nx][ny] == 0:
                next_cost = cost + (100 if i == d else 600)
                if dist[nx][ny][i] > next_cost:
                    dist[nx][ny][i] = next_cost
                    heappush(queue, (next_cost, nx, ny, i))

    return -1

# 방향 때문에 3차원 배열을 유지해야 한다.. 방향에 따라서 다음 최소 비용이 달라질 수도 있기 때문..

print(solution([[0,0,0],[0,0,0],[0,0,0]]))
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))