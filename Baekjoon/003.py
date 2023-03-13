# https://www.acmicpc.net/problem/20186

n1, n2 = map(int, input().split())
s = list(map(int, input().split()))
s.sort()

result = sum(s[len(s)-n2:len(s)])-sum(range(n2))
print(result)