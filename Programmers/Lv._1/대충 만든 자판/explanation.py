def solution(keymap, targets):
    answer = []

    key_dic = {}
    for line in keymap:
        for i, j in enumerate(line):
            if j in key_dic:
                key_dic[j] = min(key_dic[j], i + 1)
            else:
                key_dic[j] = i + 1

    for t in targets:
        sub = 0
        for i in t:
            if i in key_dic:
                sub += key_dic[i]
            else:
                sub = -1
                break
        answer.append(sub)

    return answer

print(solution(["AA"],["B"]))