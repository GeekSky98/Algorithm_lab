import sys

n = int(input())
arr = list(map(int, input().split()))
s = int(input())

index = 0
while s > 0 and index < n:
    max_value = arr[index]
    max_index = index
    for i in range(index + 1, min(n, index + s + 1)):
        if arr[i] > max_value:
            max_value = arr[i]
            max_index = i
    if index != max_index:
        arr[max_index] = arr[index]
        arr[index] = max_value
        s -= max_index - index
    index += 1

print(" ".join(map(str, arr)))


# --- 아.. 맞다.. index를 max_index로 보내는게 아니라 밀어내는 거였지..

import sys

n = int(input())
arr = list(map(int, input().split()))
s = int(input())

index = 0
while s > 0 and index < n:
    max_index = index
    for i in range(index + 1, min(n, index + s + 1)):
        if arr[i] > arr[max_index]:
            max_index = i
    if index != max_index:
        for i in range(max_index, index, -1):
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
        s -= max_index - index
    index += 1

print(" ".join(map(str, arr)))