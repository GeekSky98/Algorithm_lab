import sys
from collections import defaultdict
row, col = map(int, sys.stdin.readline().split())
table = ["".join(map(str,sys.stdin.readline().strip())) for _ in range(row)]
k = int(sys.stdin.readline())

def solution(table, k, row, col):
    answer = 0
    table_dic = defaultdict(int)
    for t in table:
        table_dic[t] += 1

    for pattern, count in table_dic.items():
        cnt = pattern.count('0')
        if cnt <= k and (k - cnt) % 2 == 0:
            answer = max(answer, count)
    return answer

print(solution(table, k, row, col))