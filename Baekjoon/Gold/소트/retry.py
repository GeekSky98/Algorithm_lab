import sys

n = int(input())
arr = list(map(int, input().split()))
s = int(input())

idx = 0
while s > 0 and idx < n:
    max_value = arr[idx]
    max_idx = idx
    for i in range(idx+1, min(n, idx+s+1)):
        if arr[i] > max_value:
            max_value = arr[i]
            max_idx = i

    if idx != max_idx:
        for i in range(max_idx, idx, -1):
            arr[i], arr[i-1] = arr[i-1], arr[i]
        s -= max_idx - idx

    idx += 1

print(" ".join(map(str, arr)))