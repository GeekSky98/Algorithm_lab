# https://www.acmicpc.net/problem/15665

n, m = map(int, input().split())
num = sorted(input().split(), key=lambda x: int(x))

arr = []
dict = {}

def result(cnt):
    if cnt == m:
        k = ' '.join(arr)
        if k not in dict:
            dict[k] = 1
            print(k)
        return

    for i in range(n):
        arr.append(num[i])
        result(cnt + 1)
        arr.pop()

result(0)