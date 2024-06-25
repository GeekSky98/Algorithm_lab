import sys

n = int(sys.stdin.readline().strip())
class_list = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

class_list.sort(key=lambda x: x[1])

cnt = 0
last_time = 0
for c in class_list:
    if c[0] >= last_time:
        cnt += 1
        last_time = c[1]

print(cnt)