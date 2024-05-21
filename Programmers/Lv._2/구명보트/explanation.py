from collections import deque
def solution(people, limit):
    answer = 0
    queue = deque(sorted(people, reverse=True))

    while len(queue) > 1:
        big = queue.popleft()
        if big + queue[-1] <= limit:
            queue.pop()
        answer += 1

    return answer + 1 if queue else answer