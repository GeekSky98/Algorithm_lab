from collections import deque

def detect(data, index, n):
    printed = 0
    p_queue = deque(sorted(data, reverse=True))
    data = deque([(i, j) for i, j in enumerate(data)])

    while True:
        target = p_queue.popleft()
        while True:
            i, v = data.popleft()
            if v == target:
                printed += 1
                break
            else:
                data.append((i, v))
        if i == index:
            break

    return printed

case = int(input())
for _ in range(case):
    n, i = map(int, input().split())
    q = list(map(int, input().split()))
    print(detect(q, i, n))