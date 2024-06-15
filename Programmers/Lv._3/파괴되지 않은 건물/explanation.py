def solution(board, skill):  # 누적합을 통한 마스크 계산
    answer = 0
    row, col = len(board), len(board[0])
    temp_arr = [[0]*(col+1) for _ in range(row+1)]  # 누적합을 위한 패딩 추가

    for inform in skill:
        type, lx, ly, rx, ry, damage = inform
        if type == 1:
            damage = -damage
        temp_arr[lx][ly] += damage
        temp_arr[rx+1][ry+1] += damage
        temp_arr[lx][ry+1] -=damage
        temp_arr[rx+1][ly] -=damage

    for i in range(row):  # 행 누적합
        for j in range(1, col):
            temp_arr[i][j] += temp_arr[i][j-1]
    for i in range(col):  # 열 누적합
        for j in range(1, row):
            temp_arr[j][i] += temp_arr[j-1][i]

    for i in range(row):
        for j in range(col):
            if board[i][j] + temp_arr[i][j] > 0:
                answer +=1

    return answer