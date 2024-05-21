from collections import deque
from heapq import heappop, heappush, heapify
def solution(n, k, enemy):
    answer = k
    if k >= len(enemy):
        return len(enemy)
    enemey = deque(enemy)
    super_card = [deque.popleft(enemey) for e in range(k)]
    heapify(super_card)
    while n > 0 and enemey:
        target = deque.popleft(enemey)
        min_super = heappop(super_card)
        if min_super < target:
            n += target - min_super
            heappush(super_card, target)
        else:
            heappush(super_card, min_super)
        if target <= n:
            n -= target
            answer += 1
        else:
            break
    return answer