import sys
from collections import defaultdict

n, m = map(int, sys.stdin.readline().split())
cars = list(map(int, sys.stdin.readline().split()))
questions = [int(sys.stdin.readline().strip()) for _ in range(m)]

cars.sort()
cnt_dic = defaultdict(int)

for j in range(1, n-1):
    left = j
    right = n - j - 1
    cnt_dic[cars[j]] = left * right

for q in questions:
    if q in cnt_dic:
        print(cnt_dic[q])
    else:
        print(0)