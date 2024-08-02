from itertools import combinations as c
n, w = int(input()), 0
for i in range(1, n+1):
    m = max(sum(x) % 10 for x in c(map(int, input().split()), 3))
    if m >= w: w, r = m, i
print(r)