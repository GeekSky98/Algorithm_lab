import sys
n, k = map(int, sys.stdin.readline().split())

answer = 0
while bin(n).count("1") > k:
    n += 1
    answer += 1

print(answer)