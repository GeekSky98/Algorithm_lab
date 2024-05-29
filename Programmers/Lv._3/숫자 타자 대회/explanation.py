from heapq import heappush, heappop

def cal_cost(x, y):
    key_arr = {
        '1': (0, 0), '2': (0, 1), '3': (0, 2),
        '4': (1, 0), '5': (1, 1), '6': (1, 2),
        '7': (2, 0), '8': (2, 1), '9': (2, 2),
        '*': (3, 0), '0': (3, 1), '#': (3, 2)
    }

    x_x, x_y = key_arr[x]
    y_x, y_y = key_arr[y]

    dx = abs(x_x - y_x)
    dy = abs(x_y - y_y)

    if dx == 0 and dy == 0:
        return 1
    elif dx == dy:
        return 3 * dx
    elif dx == 0 or dy == 0:
        return 2 * (dx + dy)
    else:
        return 3 * min(dx, dy) + 2 * abs(dx - dy)

def solution(numbers):
    queue, dp, len_num = [], {}, len(numbers)
    heappush(queue, (0, '4', '6', 0))

    while queue:
        cost, left, right, index = heappop(queue)
        if index == len_num:
            return cost

        target_num = numbers[index]

        if target_num != right:
            new_cost_left = cost + cal_cost(left, target_num)
            if (target_num, right, index + 1) not in dp or new_cost_left < dp[(target_num, right, index + 1)]:
                dp[(target_num, right, index + 1)] = new_cost_left
                heappush(queue, (new_cost_left, target_num, right, index + 1))

        if target_num != left:
            new_cost_right = cost + cal_cost(right, target_num)
            if (left, target_num, index + 1) not in dp or new_cost_right < dp[(left, target_num, index + 1)]:
                dp[(left, target_num, index + 1)] = new_cost_right
                heappush(queue, (new_cost_right, left, target_num, index + 1))