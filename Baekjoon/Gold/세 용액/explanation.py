import sys

n = int(input())
arr = sorted(list(map(int, input().split())))

def solution(n, arr):
    low_sum = float('inf')
    answer = []

    for i in range(n-2):
        left = i + 1
        right = n-1

        while left < right:
            total = arr[i] + arr[left] + arr[right]

            if abs(total) < abs(low_sum):
                low_sum = total
                answer = [arr[i], arr[left], arr[right]]

            if total == 0:
                return answer

            if total < 0:
                left += 1
            else:
                right -= 1

    return answer

print(" ".join(map(str, solution(n, arr))))