def solution(sequence):
    p1 = [j * 1 if i % 2 == 0 else j * -1 for i, j in enumerate(sequence)]  # -1로 시작
    p2 = [j * -1 if i % 2 == 0 else j * 1 for i, j in enumerate(sequence)]  # 1로 시작

    max_value = 0
    for d in [p1, p2]:
        max_sum = current_sum = d[0]
        for i in d[1:]:
            current_sum = max(current_sum + i, i)
            max_sum = max(current_sum, max_sum)

        max_value = max(max_value, max_sum)

    return max_value