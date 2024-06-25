import sys
from itertools import permutations
from collections import deque

n, basket, k = map(int, sys.stdin.readline().split())
weights = list(map(int, sys.stdin.readline().split()))

answer = float('inf')

com = permutations(weights)

for i in com:
    queue = deque(i)
    least_work = k
    total_weight = 0
    current_weight = 0

    while least_work > 0:
        if current_weight + queue[0] > basket:
            least_work -= 1
            total_weight += current_weight
            current_weight = 0
            continue

        now = queue.popleft()
        current_weight += now
        queue.append(now)

    answer = min(answer, total_weight)

print(answer)