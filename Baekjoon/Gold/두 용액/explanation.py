import sys
n = int(sys.stdin.readline())
data = sorted(list(map(int, sys.stdin.readline().split())))

left, right = 0, len(data)-1
min_sum = float("inf")
answer = (data[left], data[right])

while left < right:
    current_sum = data[left] + data[right]

    if abs(current_sum) < abs(min_sum):
        min_sum = current_sum
        answer = (data[left], data[right])

    if current_sum == 0:
        break
    elif current_sum < 0:
        left += 1
    else:
        right -= 1

print(answer[0], answer[1])