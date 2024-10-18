import sys
from bisect import bisect_left

n, h = map(int, sys.stdin.readline().split())
up, down = [], []
for i in range(1, n + 1):
    if i % 2 == 0:
        up.append(int(sys.stdin.readline()))
    else:
        down.append(int(sys.stdin.readline()))

up.sort()
down.sort()

u_len, d_len = len(up), len(down)

block = float('inf')
block_num = 1

for i in range(1, h + 1):
    up_cnt = u_len - bisect_left(up, h - i + 1)
    down_cnt = d_len - bisect_left(down, i)
    total_cnt = up_cnt + down_cnt

    if total_cnt == block:
        block_num += 1
    elif total_cnt < block:
        block_num = 1
        block = total_cnt


print(block, block_num)



temp = [1,2,3]
bisect_left(temp, 2)