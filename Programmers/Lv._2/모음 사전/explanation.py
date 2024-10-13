def solution(word):
    answer = 0
    weight = [781, 156, 31, 6, 1]
    dic = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    for i, j in enumerate(word):
        answer += dic[j] * weight[i] + 1

    return answer