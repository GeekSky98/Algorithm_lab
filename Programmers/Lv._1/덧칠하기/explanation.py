def solution(n, m, section):
    cnt = 0
    painted = 0
    for i in section:
        if i > painted:
            cnt += 1
            painted = i + m -1

    return cnt