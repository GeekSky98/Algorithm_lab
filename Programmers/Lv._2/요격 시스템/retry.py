def solution(targets):
    answer = 0
    targets.sort(key=lambda x: x[1])
    last_end = 0
    for s, e in targets:
        if s >= last_end:
            answer += 1
            last_end = e

    return answer