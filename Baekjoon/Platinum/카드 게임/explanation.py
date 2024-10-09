import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().split())
card = deque(sorted(list(map(int, sys.stdin.readline().split()))))
target = sorted(enumerate(list(map(int, sys.stdin.readline().split()))), key=lambda x: x[1])

answer = [0] * k
for i, num in target:
    while True:
        my_card = card.popleft()
        if my_card > num:
            answer[i] = my_card
            break

for i in answer:
    print(i)


# 반례
# 100 4 3
# 30 40 50 60
# 29 1 24
# 30으로 다 커버할 수 있어서 철수 카드를 정렬된 순으로 처리하면 안된다.

import sys
from bisect import bisect_right

n, m, k = map(int, sys.stdin.readline().split())
card = sorted(list(map(int, sys.stdin.readline().split())))
target = list(map(int, sys.stdin.readline().split()))

visited = [False] * len(card)

for i in target:
    card_idx = bisect_right(card, i)
    while True:
        if not visited[card_idx]:
            visited[card_idx] = True
            print(card[card_idx])
            break
        card_idx += 1