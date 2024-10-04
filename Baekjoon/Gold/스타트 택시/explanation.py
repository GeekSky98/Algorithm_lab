import sys
import heapq
from collections import deque
input = sys.stdin.readline

n, m, energy = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
x, y = map(int, input().split())
customer_list = [tuple(map(int, input().split())) for _ in range(m)]

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

c_d_dic = dict()
for a, b, c, d in customer_list:
    arr[a - 1][b - 1] = 2
    c_d_dic[(a - 1, b - 1)] = (c - 1, d - 1)

taxi_location = (x - 1, y - 1)

def find_customer(t_x, t_y):
    heap = []
    heapq.heappush(heap, (0, t_x, t_y))
    visited = [[False]*n for _ in range(n)]
    visited[t_x][t_y] = True

    while heap:
        dist, x, y = heapq.heappop(heap)
        if arr[x][y] == 2:
            return x, y, dist

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and arr[nx][ny] != 1:
                    visited[nx][ny] = True
                    heapq.heappush(heap, (dist + 1, nx, ny))
    return -1, -1, -1

def find_destination(s_x, s_y, d_x, d_y):
    queue = deque()
    queue.append((s_x, s_y, 0))
    visited = [[False]*n for _ in range(n)]
    visited[s_x][s_y] = True

    while queue:
        x, y, dist = queue.popleft()
        if x == d_x and y == d_y:
            return dist

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and arr[nx][ny] != 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))
    return -1

def solution():
    global energy, taxi_location
    for _ in range(m):
        c_x, c_y, dist_to_customer = find_customer(taxi_location[0], taxi_location[1])
        if c_x == -1 or dist_to_customer > energy:
            return -1

        energy -= dist_to_customer
        taxi_location = (c_x, c_y)

        dest_x, dest_y = c_d_dic[(c_x, c_y)]
        arr[c_x][c_y] = 0

        dist_to_destination = find_destination(c_x, c_y, dest_x, dest_y)
        if dist_to_destination == -1 or dist_to_destination > energy:
            return -1

        energy += dist_to_destination * 2 - dist_to_destination

        taxi_location = (dest_x, dest_y)
        del c_d_dic[(c_x, c_y)]

    return energy

print(solution())
