import sys

n, m = map(int, input().split())
data = [list(sys.stdin.readline().strip()) for _ in range(n)]

MAX = 1
MIN = min(n, m)

for i in range(n):
    for j in range(m):
        for k in range(1, MIN):
            if i + k < n and j + k < m:
                if data[i][j] == data[i][j+k] == data[i+k][j] == data[i+k][j+k]:
                    MAX = max((k+1) ** 2, MAX)

print(MAX)