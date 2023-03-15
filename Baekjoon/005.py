# https://www.acmicpc.net/problem/10816

import sys

input = sys.stdin.readline
N = int(input())
a = map(int, input().split())

hash = {}
for num in a:
    hash[num] = hash.setdefault(num, 0) + 1

M = int(input())
b = map(int, input().split())
for num in b :
    print(hash.setdefault(num, 0), end = ' ')