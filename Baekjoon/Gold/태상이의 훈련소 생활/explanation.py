import sys

n, m = map(int, sys.stdin.readline().split())
land = list(map(int, sys.stdin.readline().split()))
act = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]

diff_land = [0] * (n+1)

for s, e, c in act:
    diff_land[s-1] += c
    if e < n:
        diff_land[e] -= c

current = 0
for i in range(n):
    current += diff_land[i]
    land[i] += current

print(" ".join(map(str, land)))