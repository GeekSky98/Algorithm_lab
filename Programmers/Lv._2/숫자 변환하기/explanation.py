from collections import deque
def solution(x, y, n):
    if x == y:
        return 0
    queue = deque([(x, 0)])
    visited = set([x])
    while queue:
        num, cnt = queue.popleft()

        cals = [num + n, num * 2, num * 3]
        for cal in cals:
            if cal == y:
                return cnt + 1
            if cal < y and cal not in visited:
                visited.add(cal)
                queue.append((cal, cnt+1))
    return -1

solution(10,40,30)