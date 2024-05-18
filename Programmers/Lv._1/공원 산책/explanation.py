def solution(park, routes):
    width, height = len(park), len(park[0])
    dir_dic = {"N": [-1, 0], "S": [1, 0], "W": [0, -1], "E": [0, 1]}
    x_list = []
    for i in range(width):
        for j in range(height):
            if park[i][j] == "S":
                start = [i, j]
            elif park[i][j] == "X":
                x_list.append([i, j])
    for r in routes:
        d, n = r.split(' ')
        go_flag = True
        for i in range(1, int(n) + 1):
            next = [start[0] + (dir_dic[d][0] * i), start[1] + (dir_dic[d][1] * i)]
            if next in x_list or not 0 <= next[0] < width or not 0 <= next[1] < height:
                go_flag = False
        if go_flag:
            start = next

    return start