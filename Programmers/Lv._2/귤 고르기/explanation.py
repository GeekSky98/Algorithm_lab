def solution(k, tangerine):
    answer, idx, cnt_dic = 0, 0, {}
    for i in tangerine:
        if i in cnt_dic:
            cnt_dic[i] += 1
        else:
            cnt_dic[i] = 1
    value = sorted(list(cnt_dic.values()), reverse=True)
    while k > 0:
        answer += 1
        k -= value[idx]
        idx += 1

    return answer