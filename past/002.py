# https://www.acmicpc.net/problem/1920

import sys

input = sys.stdin.readline

def binary_search(array, target):
    start, end = 0, len(array)-1

    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return 1
        elif target < array[mid]:
            end = mid-1
        else :
            start = mid+1
    return 0

N = int(input())
nums = list(map(int, input().split()))
nums.sort()

M = int(input())
nums2 = list(map(int, input().split()))

for target in nums2:
    print(binary_search(nums, target))