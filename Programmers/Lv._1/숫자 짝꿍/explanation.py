from collections import Counter

def solution(X, Y):
    x_cnt = Counter(X)
    y_cnt = Counter(Y)

    answer = ''
    for i in '9876543210':
        if i in x_cnt and i in y_cnt:
            answer += i * min(x_cnt[i], y_cnt[i])

    if not answer:
        return "-1"
    elif answer[0] == '0':
        return "0"
    else:
        return "".join(answer)