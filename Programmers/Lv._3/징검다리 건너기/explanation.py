from collections import deque


def solution(stones, k):
    dq = deque()
    max_list = []

    for i in range(k):
        while dq and stones[dq[-1]] <= stones[i]:
            dq.pop()
        dq.append(i)

    max_list.append(stones[dq[0]])

    for i in range(k, len(stones)):

        while dq and dq[0] <= i - k:
            dq.popleft()

        while dq and stones[dq[-1]] <= stones[i]:
            dq.pop()

        dq.append(i)

        max_list.append(stones[dq[0]])

    return min(max_list)