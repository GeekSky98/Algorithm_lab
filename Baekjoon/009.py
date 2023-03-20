# https://www.acmicpc.net/problem/11478

s = input()
result = []

for i in range(len(s)):
    for j in range(i, len(s)):
        result.append(s[i:j + 1])

print(len(set(result)))