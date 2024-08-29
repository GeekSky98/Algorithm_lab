import sys
n = int(sys.stdin.readline())
data = sorted(list(map(int, sys.stdin.readline().split())))

possible_num = 0
for i in data:
    if possible_num + 1 < i:
        break
    possible_num += i

print(possible_num+1)