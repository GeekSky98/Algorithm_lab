import sys
a, b = map(int, sys.stdin.readline().split())

def detect(num):
    cnt = 0
    i = 0
    while (1 << i) <= num:
        cycle = 1 << (i + 1)
        full_block = num // cycle
        cnt += full_block * (1 << i)

        remainder = num % cycle
        if remainder >= (1 << i):
            cnt += remainder - (1 << i) + 1
        i += 1
    return cnt

print(detect(b) - detect(a-1))