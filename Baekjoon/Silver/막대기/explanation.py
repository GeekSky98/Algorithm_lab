import sys
from collections import deque
n = int(sys.stdin.readline())

def solution(x):
    wood = deque([64, 32, 16, 8, 4, 2, 1])
    if x in wood:
        return 1

    cnt = 0
    if x % 2 != 0:
        cnt += 1
        x -= 1

    while x > 1:
        if x < wood[0]:
            wood.popleft()
            continue
        x -= wood[0]
        cnt += 1

    return cnt

print(solution(n))