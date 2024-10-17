import sys
from collections import deque
from itertools import permutations

n = int(sys.stdin.readline())
games = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def baseball(score):
    max_score = 0
    orders = [i for i in range(1, 9)]
    for order in permutations(orders, 8):
        order_list = list(order[:3]) + [0] + list(order[3:])
        now_score = 0
        i = 0
        for s in score:
            b1 = b2 = b3 = 0
            out_cnt = 0
            while out_cnt < 3:
                now = s[order_list[i % 9]]
                i += 1

                if now == 0:
                    out_cnt += 1
                elif now == 1:
                    now_score += b3
                    b3, b2, b1 = b2, b1, 1
                elif now == 2:
                    now_score += b2 + b3
                    b3, b2, b1 = b1, 1, 0
                elif now == 3:
                    now_score += b1 + b2 + b3
                    b3, b2, b1 = 1, 0, 0
                else:
                    now_score += b1 + b2 + b3 + 1
                    b1 = b2 = b3 = 0

        max_score = max(max_score, now_score)

    return max_score

print(baseball(games))

# 너무 무식한 문제였다.. python으로는 풀리지도 않고, pypy3 이용해야 한다.