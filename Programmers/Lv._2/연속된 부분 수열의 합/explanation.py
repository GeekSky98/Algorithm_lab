def solution(sequence, k):
    min_len = float('inf')
    left = right = 0
    sub_sum = sequence[0]
    answer = []

    while right < len(sequence):
        if sub_sum == k:
            if right - left < min_len:
                min_len = right - left
                answer = [left, right]
            sub_sum -= sequence[left]
            left += 1
        elif sub_sum < k:
            right += 1
            if right < len(sequence):
                sub_sum += sequence[right]
        else:
            sub_sum -= sequence[left]
            left += 1

    return answer

print(solution([2, 2, 2, 2, 2], 2))