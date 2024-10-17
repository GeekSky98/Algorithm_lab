def solution(babbling):
    possible = ["aya", "ye", "woo", "ma"]
    cnt = 0
    for i in babbling:
        for p in possible:
            if p * 2 not in i:
                i = i.replace(p, ' ')
        if len(i.strip()) == 0:
            cnt += 1

    return cnt