import sys

n = int(sys.stdin.readline().strip())
score = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]

def cal_rank(N, s_list):
    sort_list = sorted(enumerate(s_list), key = lambda x: x[1], reverse = True)
    result = [0] * N
    for index, (i, s) in enumerate(sort_list):
        if index > 0 and sort_list[index-1][1] == s:
            result[i] = result[sort_list[index-1][0]]
        else:
            result[i] = index + 1
    return " ".join(map(str, result))

score.append([sum(score[i][j] for i in range(3)) for j in range(n)])

for sc in score:
    print(cal_rank(n, sc))