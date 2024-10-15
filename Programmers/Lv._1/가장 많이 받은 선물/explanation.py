def solution(friends, gifts):
    present_dic = {friend: {f: 0 for f in friends} for friend in friends}
    score_dic = {f: 0 for f in friends}

    for g in gifts:
        a, b = g.split()
        present_dic[a][b] += 1
        score_dic[a] += 1
        score_dic[b] -= 1

    max_present = 0
    for now in friends:
        sub = 0
        for friend in friends:
            if friend == now:
                continue
            if present_dic[now][friend] > present_dic[friend][now]:
                sub += 1
            elif present_dic[now][friend] == present_dic[friend][now] and score_dic[now] > score_dic[friend]:
                sub += 1
        max_present = max(max_present, sub)

    return max_present