def solution(genres, plays):
    answer = []
    inform_dic = {}
    count_dic = {}

    for i, (g, p) in enumerate(zip(genres, plays)):
        if g in inform_dic:
            inform_dic[g].append((i, p))
            count_dic[g] += p
        else:
            inform_dic[g] = [(i, p)]
            count_dic[g] = p

    for key, _ in sorted(count_dic.items(), key = lambda x: x[1], reverse=True):
        for index, _ in sorted(inform_dic[key], key = lambda x: x[1], reverse=True)[:2]:
            answer.append(index)

    return answer