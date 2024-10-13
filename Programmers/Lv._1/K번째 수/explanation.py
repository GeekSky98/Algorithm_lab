def solution(array, commands):
    answer = []
    [answer.append(sorted(array[i-1:j])[k-1]) for i, j, k in commands]
    return answer