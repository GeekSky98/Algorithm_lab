from collections import defaultdict
def solution(picks, minerals):
    answer = 0
    total_picks = sum(picks)
    p_type = ['diamond', 'iron', 'stone']
    p_map = {
        'diamond': {'diamond': 1, 'iron': 1, 'stone': 1},
        'iron': {'diamond': 5, 'iron': 1, 'stone': 1},
        'stone': {'diamond': 25, 'iron': 5, 'stone': 1}
    }

    group_dic, mineral_dic = defaultdict(int), defaultdict(list)
    for i, m in enumerate(minerals):
        index = i // 5
        if index >= total_picks:
            break
        if m == "diamond":
            group_dic[index] += 25
        elif m == "iron":
            group_dic[index] += 5
        else:
            group_dic[index] += 1
        mineral_dic[index].append(m)

    rank_index = sorted(group_dic, key=lambda x: group_dic[x])
    for i, p in enumerate(picks):
        for _ in range(p):
            if rank_index:
                for t in mineral_dic[rank_index.pop()]:
                    answer += p_map[p_type[i]][t]

    return answer