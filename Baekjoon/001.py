# https://www.acmicpc.net/problem/1018

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

maps = list()
answer = []

for _ in range(N):
    maps.append(list(input().rstrip()))

for r in range(N - 8 + 1):
    for c in range(M - 8 + 1):
        start = maps[r][c]

        countB = 0
        countW = 0

        for r_idx, n in enumerate(maps[r:r + 8]):
            for c_idx, m in enumerate(n[c:c + 8]):
                if (r_idx + c_idx) % 2 == 0:
                    if m != 'B':
                        countB += 1
                else:
                    if m != 'W':
                        countB += 1

                if (r_idx + c_idx) % 2 == 0:
                    if m != 'W':
                        countW += 1
                else:
                    if m != 'B':
                        countW += 1

                count = min(countB, countW)

        answer.append(count)

print(min(answer))