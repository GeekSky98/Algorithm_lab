import sys
from collections import defaultdict

t = int(input())
n = int(input())
list_1 = list(map(int, input().split()))
m = int(input())
list_2 = list(map(int, input().split()))

def arr_sum(arr):
    length = len(arr)
    sum_list = []

    for i in range(length):
        total = 0
        for j in range(i, length):
            total += arr[j]
            sum_list.append(total)

    return sum_list

a_sum = arr_sum(list_1)
b_sum = arr_sum(list_2)

a_dic = defaultdict(int)
for i in a_sum:
    a_dic[i] += 1

count = 0
for i in b_sum:
    if t - i in a_dic:
        count += a_dic[t-i]

print(count)