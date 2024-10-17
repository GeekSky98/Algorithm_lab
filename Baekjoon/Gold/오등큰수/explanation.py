import sys
from collections import Counter

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

cnt_dic = Counter(data)
stack = []
answer = [-1] * n

for i in range(n):
    while stack and cnt_dic[data[stack[-1]]] < cnt_dic[data[i]]:
        answer[stack.pop()] = data[i]

    stack.append(i)

print(" ".join(map(str, answer)))