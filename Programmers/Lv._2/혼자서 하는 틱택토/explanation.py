def bingo(targets):
    for i in range(3):
        if (i, 0) in targets and (i, 1) in targets and (i, 2) in targets:
            return True
        if (0, i) in targets and (1, i) in targets and (2, i) in targets:
            return True
    if (0, 0) in targets and (1, 1) in targets and (2, 2) in targets:
        return True
    if (0, 2) in targets and (1, 1) in targets and (2, 0) in targets:
        return True
    return False

def solution(board):
    index_dic = {'X': [], 'O': []}
    for i, piece in enumerate(board):
        for j in range(3):
            if piece[j] == 'X':
                index_dic['X'].append((i, j))
            elif piece[j] == 'O':
                index_dic['O'].append((i, j))
    x_cnt, o_cnt = len(index_dic['X']), len(index_dic['O'])
    x_bingo, o_bingo = bingo(index_dic['X']), bingo(index_dic['O'])
    if x_cnt > o_cnt or abs(x_cnt - o_cnt) > 1 or (x_bingo and o_bingo) or (o_bingo and o_cnt != x_cnt + 1) or (x_bingo and x_cnt != o_cnt):
        return 0
    return 1