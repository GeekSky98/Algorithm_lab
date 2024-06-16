def solution(a):
    answer = 0
    q_len = len(a)

    dp_left = [float('inf')] * q_len
    dp_right = [float('inf')] * q_len
    dp_left[0], dp_right[-1] = a[0], a[-1]

    for i in range(1, q_len):
        dp_left[i] = min(dp_left[i-1], a[i])

    for i in range(q_len-2, 0, -1):
        dp_right[i] = min(dp_right[i+1], a[i])

    for i, num in enumerate(a):
        if num > dp_left[i] and num > dp_right[i]:
            continue
        else:
            answer += 1

    return answer