def solution(n):
    a, b = 0, 1
    for _ in range(n):
        now = a+b
        a, b = b, now
    return now % 1234567