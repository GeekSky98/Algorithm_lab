import sys
n, k = map(int, sys.stdin.readline().split())
score = list(map(int, sys.stdin.readline().split()))
range_list = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]

'''
for start, end in range_list:
    temp = 0
    for i in range(start-1, end):
        temp += score[i]
    print(round((temp / (end-start+1)), 2))
'''

prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + score[i - 1]

for start, end in range_list:
    print(round((prefix[end] - prefix[start-1]) / (end-start+1), 2))