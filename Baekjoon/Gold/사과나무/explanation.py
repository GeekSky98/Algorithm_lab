import sys

_ = int(input())
heights = list(map(int, sys.stdin.readline().split()))

total_height = sum(heights)

if total_height % 3 == 0:
    count = sum(height // 2 for height in heights)
    if count >= total_height / 3:
        print("YES")
    else:
        print("NO")
else:
    print("NO")