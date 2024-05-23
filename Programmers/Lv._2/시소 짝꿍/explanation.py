from collections import Counter

def solution(weights):
    answer = 0

    cnt_dic = Counter(weights)
    for k, v in cnt_dic.items():
        if v >= 2:
            answer += v * (v-1) // 2

    weights = set(weights)

    for weight in weights:
        if weight * 1/2 in weights:
            answer += cnt_dic[weight*1/2] * cnt_dic[weight]
        if weight * 2/3 in weights:
            answer += cnt_dic[weight*2/3] * cnt_dic[weight]
        if weight * 3/4 in weights:
            answer += cnt_dic[weight*3/4] * cnt_dic[weight]

    return answer