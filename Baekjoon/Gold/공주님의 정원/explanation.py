import sys
n = int(input())
def to_int(n_list):
    return (n_list[0] * 100 + n_list[1], n_list[2] * 100 + n_list[3])
arr = [to_int(list(map(int, input().split()))) for i in range(n)]

limit_start, limit_end = 301, 1130
arr.sort(key=lambda x: (x[0], -x[1]))

index = 0
cnt = 0
last_start = current_end = limit_start
possible_flag = True
while possible_flag and index < n:
    find_flag = False
    while index < n and arr[index][0] <= last_start:
        current_end = max(current_end, arr[index][1])
        index += 1
        find_flag = True

    if not find_flag:
        possible_flag = False
        break

    cnt += 1
    last_start = current_end
    if last_start > limit_end:
        print(cnt)
        break

if last_start <= limit_end:
    print(0)