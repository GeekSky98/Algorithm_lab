from collections import deque
def solution(queue1, queue2):
    answer = 0
    q_len = len(queue1)
    q1, q2 = sum(queue1), sum(queue2)
    total = q1 + q2

    if total % 2 != 0:
        return -1

    div = total // 2
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    while q1 != div:
        if q1 > div:
            num1 = queue1.popleft()
            q1 -= num1
            queue2.append(num1)
        else:
            num2 = queue2.popleft()
            q1 += num2
            queue1.append(num2)
        answer += 1
        if answer > q_len*3:
            return -1

    return answer