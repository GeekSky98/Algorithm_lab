from heapq import heappop, heappush


def solution(n, k, enemy):
    e_len = len(enemy)
    if e_len <= k:
        return e_len

    queue = []
    cnt = 0
    for i in range(k):
        heappush(queue, enemy[i])
        cnt += 1

    index = k
    while n > 0 and index < e_len:
        now = enemy[index]
        min_shield = heappop(queue)
        if now > min_shield:
            n -= min_shield
            heappush(queue, now)
        else:
            n -= now
            heappush(queue, min_shield)
        if n >= 0:
            cnt += 1
        index += 1

    return cnt