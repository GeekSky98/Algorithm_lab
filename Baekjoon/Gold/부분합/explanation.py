import sys
n, s = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

left_point = right_point = current_sum = 0
min_length = float('inf')
for right_point in range(n):
    current_sum += nums[right_point]

    while current_sum >= s:
        min_length = min(min_length, right_point-left_point+1)
        current_sum -= nums[left_point]
        left_point += 1

print(min_length if min_length != float('inf') else 0)

