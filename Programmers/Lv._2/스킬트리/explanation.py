def solution(skill, skill_trees):
    skill_dic = {s: i for i, s in enumerate(skill)}
    answer = 0
    for tree in skill_trees:
        flag = True
        prev_num = 0
        for s in tree:
            if s not in skill_dic:
                continue
            if skill_dic[s] == prev_num:
                prev_num += 1
            else:
                flag = False
                break
        if flag:
            answer += 1

    return answer