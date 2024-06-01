from itertools import combinations
def solution(relation):
    row = len(relation)
    col = len(relation[0])

    all_case = [com for col_ea in range(1, col + 1) for com in combinations(range(col), col_ea)]

    matched_case = []
    for case in all_case:
        target = set([tuple([rows[i] for i in case]) for rows in relation])
        if len(target) == row:
            match_flag = True
            for matched in matched_case:
                if set(matched).issubset(set(case)):
                    match_flag = False
                    break
            if match_flag:
                matched_case.append(case)

    return len(matched_case)