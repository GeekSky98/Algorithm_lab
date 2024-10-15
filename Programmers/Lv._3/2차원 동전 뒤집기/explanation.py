from collections import deque
from copy import deepcopy

def solution(beginning, target):
    x_len = len(beginning)
    y_len = len(beginning[0])

    visited = set()
    visited.add(tuple(map(tuple, beginning)))
    queue = deque([(beginning, 0)])

    while queue:
        arr, cost = queue.popleft()

        if arr == target:
            return cost

        for i in range(x_len):
            next_arr = deepcopy(arr)
            for j in range(y_len):
                next_arr[i][j] = 1 - next_arr[i][j]
            tuple_arr = tuple(map(tuple, next_arr))
            if not tuple_arr in visited:
                queue.append((next_arr, cost + 1))
                visited.add(tuple_arr)

        for i in range(y_len):
            next_arr = deepcopy(arr)
            for j in range(x_len):
                next_arr[j][i] = 1 - next_arr[j][i]
            tuple_arr = tuple(map(tuple, next_arr))
            if not tuple_arr in visited:
                queue.append((next_arr, cost + 1))
                visited.add(tuple_arr)

    return -1

# 시간초과 - 비트마스크 필요


print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]],[[1, 0, 1], [0, 0, 0], [0, 0, 0]]))
print(solution([[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]],[[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]))