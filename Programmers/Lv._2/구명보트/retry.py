from collections import deque

def solution(people, limit):
    queue = deque(sorted(people, reverse=True))

    answer = 0
    while queue:
        target = queue.popleft()

        if queue and queue[-1] + target <= limit:
            queue.pop()

        answer += 1

    return answer