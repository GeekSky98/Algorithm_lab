import sys
from collections import defaultdict
N = int(sys.stdin.readline())
A = [list(sys.stdin.readline().strip()) for _ in range(N)]

def solution(alpha, n):
    weight = defaultdict(int)

    for a in alpha:
        a_len = len(a)
        for i, num in enumerate(a):
            weight[num] += 10 ** (a_len - i -1)

    weight_sort = sorted(weight, key=lambda x: weight[x], reverse=True)

    num_dic = {}
    num = 9
    for w in weight_sort:
        num_dic[w] = num
        num -= 1

    result = ["".join([str(num_dic[j]) for j in i]) for i in alpha]
    print(sum(map(int, result)))

solution(A, N)