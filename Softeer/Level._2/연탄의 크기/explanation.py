import sys
from collections import defaultdict

n = int(sys.stdin.readline().strip())
house = list(map(int, sys.stdin.readline().split()))

div_dic = defaultdict(int)
for i in house:
    for j in range(2, i+1):
        if i % j == 0:
            div_dic[j] += 1

print(max(div_dic.values()))