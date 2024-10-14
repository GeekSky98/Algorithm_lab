def solution(n):
    total_cnt = 1
    for i in range(1, n):
        sub = 0
        for j in range(i, n):
            sub += j
            if sub == n:
                total_cnt += 1
                break
            elif sub > n:
                break
    return total_cnt