import sys
from collections import deque
import time

monkey, dog = map(int, sys.stdin.readline().split())

def solution(monkey, dog):
    if monkey == dog:
        return 0
    elif dog - monkey == 1:
        return 1
    elif dog - monkey == 2:
        return 2

    directions = [-1, 0, 1]
    queue = deque([(monkey+1, 1, 1)]) # 현재 원숭이 키, 마지막 늘린 길이, 일 수
    visited = set()
    visited.add((monkey+1, 1))

    while queue:
        monkey_now, last_len, days = queue.popleft()

        if monkey_now == dog-1:
            return days + 1

        for d in directions:
            next_plus = last_len + d
            next_monkey = monkey_now + next_plus
            if next_plus > 0 and (next_monkey, next_plus) not in visited:
                queue.append((next_monkey, next_plus, days + 1))
                visited.add((next_monkey, next_plus))

print(solution(monkey, dog))