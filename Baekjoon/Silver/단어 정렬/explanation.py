n = int(input())
data = sorted(set(input().strip() for _ in range(n)), key=lambda x: (len(x), x))
for i in data:
    print(i)