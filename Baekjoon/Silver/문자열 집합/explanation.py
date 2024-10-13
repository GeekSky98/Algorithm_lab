import sys
n, m = map(int, input().split())
a = set(input().strip() for _ in range(n))
b = [input().strip() for _ in range(m)]
cnt = 0
for i in b:
    if i in a:
        cnt += 1
print(cnt)