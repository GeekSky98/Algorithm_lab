def solution(n, stations, w):
    answer = 0
    possible = 1 + w * 2

    origin_list = []
    for s in stations:
        start = max(1, s - w)
        end = min(n, s + w)
        origin_list.append((start, end))

    current = 1
    for s, e in origin_list:
        if s > current:
            cnt, d = divmod((s - current), possible)
            if d:
                cnt += 1
            answer += cnt
        current = e + 1

    if current <= n:
        cnt, d = divmod((n - current), possible)
        if d or current == n:
            cnt += 1
        answer += cnt

    return answer