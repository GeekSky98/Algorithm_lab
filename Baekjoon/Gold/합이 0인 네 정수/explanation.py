import sys
from collections import defaultdict
n = int(input())
a, b, c, d = [], [], [], []
for _ in range(n):
    q, w, e, r = map(int, sys.stdin.readline().split())
    a.append(q); b.append(w); c.append(e); d.append(r)

ab_dic = defaultdict(int)
for i in a:
    for j in b:
        ab_dic[i + j] += 1

answer = 0
for i in c:
    for j in d:
        answer += ab_dic[-(i + j)]

print(answer)

# 뭐 때문에 시간초과인거지..