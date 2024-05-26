def solution(n):
    direction = [(0, 1), (1, 0), (-1, -1)]
    t = [[0]*i for i in range(1, n+1)]
    num = 1
    x = y = dir_index = 0

    while True:
        xp, yp = direction[dir_index % 3]
        while True:
            t[y][x] = num
            num += 1

            next_x, next_y = x + xp, y + yp

            if next_x < 0 or next_y < 0 or next_x > next_y or next_y >= n or t[next_y][next_x] != 0:
                break

            x, y = next_x, next_y

        dir_index += 1
        x, y = x+direction[dir_index % 3][0], y+direction[dir_index % 3][1]
        if x > y or y >= n or x < 0 or y < 0 or t[y][x] != 0:
            break

    answer = []
    for i in t:
        answer.extend(i)
    return answer