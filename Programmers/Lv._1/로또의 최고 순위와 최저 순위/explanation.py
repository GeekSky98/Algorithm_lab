def solution(lottos, win_nums):
    zero_cnt = ok_cnt = 0
    for l in lottos:
        if l == 0:
            zero_cnt += 1
        elif l in win_nums:
            ok_cnt += 1
    return [7 - (ok_cnt + zero_cnt) if (ok_cnt + zero_cnt) > 1 else 6, 7 - ok_cnt if ok_cnt > 1 else 6]

solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19])
solution([0, 0, 0, 0, 0, 0],[38, 19, 20, 40, 15, 25])
solution([45, 4, 35, 20, 3, 9],[20, 9, 3, 45, 4, 35])