from collections import deque


def is_valid(before_list, new_row, new_col):
    for x, y in before_list:
        if y == new_col or abs(x - new_row) == abs(y - new_col):
            return False
    return True


def solution(n):
    answer = 0

    queue = deque([])
    for i in range(n):
        queue.append(([(0, i)], 1))

    while queue:
        location, row = queue.popleft()

        if row == n:
            answer += 1

        for c in range(n):
            if is_valid(location, row, c):
                next_location = location + [(row, c)]
                queue.append((next_location, row + 1))

    return answer