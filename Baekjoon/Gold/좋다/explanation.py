import sys
n = int(sys.stdin.readline())
data = sorted(list(map(int, sys.stdin.readline().split())))
cnt = 0

for i in range(n):
    num = data[i]
    left = 0
    right = n-1

    while left < right:
        if left == i:
            left += 1
            continue
        if right == i:
            right -= 1
            continue

        current_sum = data[left] + data[right]

        if current_sum == num:
            cnt += 1
            break
        elif current_sum < num:
            left += 1
        else:
            right -= 1

print(cnt)