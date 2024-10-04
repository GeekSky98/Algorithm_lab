import sys
n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

tetrominoes = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (0, 1), (1, 0), (1, 1)],
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 1), (1, 1), (2, 1), (2, 0)],
    [(0, 0), (0, 1), (0, 2), (1, 0)],
    [(0, 2), (1, 2), (2, 2), (2, 1)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (1, 1), (1, 2)],
    [(1, 0), (0, 1), (1, 1), (2, 0)],
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(1, 0), (1, 1), (0, 1), (0, 2)],
    [(0, 1), (1, 0), (1, 1), (1, 2)],
    [(0, 1), (1, 0), (1, 1), (2, 1)],
    [(1, 0), (1, 1), (1, 2), (2, 1)],
    [(0, 1), (1, 1), (1, 0), (2, 1)]
]

max_value = 0
for i in range(n):
    for j in range(m):
        for t in tetrominoes:
            temp_sum = 0
            possible_flag = True
            for tx, ty in t:
                dx, dy = i + tx, j + ty
                if 0 <= dx < n and 0 <= dy < m:
                    temp_sum += arr[dx][dy]
                else:
                    possible_flag = False
                    break
            if possible_flag:
                max_value = max(max_value, temp_sum)

print(max_value)
