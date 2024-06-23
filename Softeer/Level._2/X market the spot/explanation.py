import sys
n = int(sys.stdin.readline().strip())
str_list = [list(sys.stdin.readline().split()) for _ in range(n)]

result = []

'''
for s, t in str_list:
    result.append(t[s.upper().index("X")].upper())
'''

for i in range(n):
    s, t = str_list[i]
    for index, char in enumerate(s):
        if char == "X" or char == "x":
            result.append(t[index].upper())
            break


print("".join(result))














