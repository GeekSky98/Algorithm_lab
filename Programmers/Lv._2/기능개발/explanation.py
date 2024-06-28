from collections import deque
from math import ceil
def solution(progresses, speeds):
    answer = []

    queue = deque()

    for p, s in zip(progresses, speeds):
        queue.append(ceil((100-p)/s))

    while queue:
        now = queue.popleft()
        cnt = 1

        while queue and queue[0] <= now:
            queue.popleft()
            cnt += 1

        answer.append(cnt)

    return answer

solution([93, 30, 55], 	[1, 30, 5])
solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])