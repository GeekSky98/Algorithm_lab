import sys
n = int(input())
player = list(map(int, sys.stdin.readline().split()))

max_value = 1000000
score = [0] * n
index_list = [-1] * (max_value + 1)

for i in range(n):
    index_list[player[i]] = i

for p in player:
    p_idx = index_list[p]
    for m in range(p * 2, max_value + 1, p):
        m_idx = index_list[m]
        if m_idx != -1:
            score[p_idx] += 1
            score[m_idx] -= 1

print(" ".join(map(str, score)))