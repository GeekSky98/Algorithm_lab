import sys
n = int(input())
data = list(map(int, input().split()))

left, right = 0, n-1
min_value = float('inf')
answer = ()
while left < right:
    pos = data[left] + data[right]
    pos_abs = abs(pos)
    if pos_abs < min_value:
        min_value = pos_abs
        answer = (data[left], data[right])

    if pos == 0:
        answer = (data[left], data[right])
        break
    elif pos < 0:
        left += 1
    else:
        right -= 1

print(" ".join(map(str, answer)))