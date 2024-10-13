from collections import deque
def solution(priorities, location):
    p = deque((i, j) for i, j in enumerate(priorities))
    answer = 0
    while p:
        index, now = p.popleft()
        if any(now < i[1] for i in p):
            p.append((index, now))
        else:
            answer += 1
            if index == location:
                return answer
