import sys

N = int(sys.stdin.readline())

def solution(n):
    if n % 5 == 0:
        return n // 5

    num = n // 5

    for i in range(num, -1, -1):
        div = n - (i * 5)
        if div % 3 == 0:
            return i + div // 3

    return -1

print(solution(N))