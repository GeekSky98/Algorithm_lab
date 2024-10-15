def solution(answers):
    type1 = [1, 2, 3, 4, 5] * 8
    type2 = [2, 1, 2, 3, 2, 4, 2, 5] * 5
    type3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 4

    idx = 0
    score = [0] * 3
    for q in answers:
        if q == type1[idx]: score[0] += 1
        if q == type2[idx]: score[1] += 1
        if q == type3[idx]: score[2] += 1
        idx += 1
        if idx == 40: idx = 0

    answer = []
    max_score = max(score)
    for i, s in enumerate(score):
        if s == max_score:
            answer.append(i + 1)

    return answer

print(solution([1,3,2,4,2]))