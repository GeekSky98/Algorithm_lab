import sys
from collections import deque

n = int(input())
queue = deque(sorted([int(input().strip()) for _ in range(n)], reverse=True))

def solution(n, queue):
    result = 0
    while queue:
        first_num = queue.popleft()
        if queue:
            second_num = queue.popleft()
        else:
            result += first_num
            continue
        result += max(first_num*second_num, first_num+second_num)

    return result

print(solution(n, queue))

# 음수와 0에 대한 고려가 안들어감.

import sys
from collections import deque

n = int(input())
data = [int(input().strip()) for _ in range(n)]

plus_list, minus_list = [], []
result = zero_cnt = 0
for i in data:
    if i > 1:
        plus_list.append(i)
    elif i == 1:
        result += 1
    elif i == 0:
        zero_cnt += 1
    else:
        minus_list.append(i)
plus_list.sort(reverse=True)
minus_list.sort()

if len(plus_list) % 2 != 0:
    result += plus_list.pop()

if len(minus_list) % 2 != 0:
    v = minus_list.pop()
    if not zero_cnt:
        result += v

plus_queue, minus_queue = deque(plus_list), deque(minus_list)
while plus_queue or minus_queue:
    if plus_queue:
        result += plus_queue.popleft() * plus_queue.popleft()
    if minus_queue:
        result += minus_queue.popleft() * minus_queue.popleft()

print(result)
