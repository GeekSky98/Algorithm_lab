from collections import deque

def solution(priorities, location):
    p = deque((i, j) for i, j in enumerate(priorities))
    p_s = sorted(priorities, reverse=True)

    cnt = 0
    for m in p_s:
        while p:
            i, n = p.popleft()
            if n == m:
                cnt += 1
                if i == location:
                    return cnt
                break
            else:
                p.append((i, n))