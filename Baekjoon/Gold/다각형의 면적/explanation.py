import sys

n = int(input())
inform = [tuple(map(int, input().split())) for _ in range(n)]

area = 0
for i in range(n):
    x, y = inform[i]
    x2, y2 = inform[(i + 1) % n]
    area += x*y2 - y*x2

print(abs(area) / 2)