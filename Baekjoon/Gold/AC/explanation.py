import sys
from collections import deque

t = int(input())
cases = []
for _ in range(t):
    func = input().strip()
    arr_len = int(input().strip())
    arr_str = input().strip()

    if arr_len == 0:
        arr = deque()
    else:
        arr = deque(map(int, arr_str[1:-1].split(',')))

    cases.append((func, arr_len, arr))

def solution(func, arr_len, arr):
    if func.count("D") > arr_len:
        return "error"

    reverse_flag = False
    for f in list(func):
        if f == 'R':
            reverse_flag = not reverse_flag
        else:
            if arr:
                if reverse_flag:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                return "error"
    if reverse_flag:
        arr.reverse()

    return "[" + ",".join(map(str, arr)) + "]"

for f, l, a in cases:
    print(solution(f, l, a))