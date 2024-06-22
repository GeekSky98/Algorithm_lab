def solution(scores):
    answer = 1
    a, b = scores[0]
    my_score = a + b
    sorted_score = sorted(scores, key=lambda x: [-x[0], x[1]])

    last_score = 0
    for i, j in sorted_score:
        if a < i and b < j:
            return -1

        if j >= last_score:
            last_score = j
            if i+j > my_score:
                answer += 1

    return answer