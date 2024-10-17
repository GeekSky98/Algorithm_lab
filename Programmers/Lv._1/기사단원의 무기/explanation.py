def solution(number, limit, power):
    cnt_list = [0] * (number + 1)
    for i in range(1, number + 1):
        for j in range(i, number + 1, i):
            cnt_list[j] += 1

    answer = []
    for i in range(1, number + 1):
        v = cnt_list[i]
        if v > limit:
            answer.append(power)
        else:
            answer.append(v)

    return sum(answer)