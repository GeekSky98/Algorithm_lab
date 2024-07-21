import sys

N = int(sys.stdin.readline())
rib = list(map(int, sys.stdin.readline().split()))

def solution(n, arr):
    answer = sorted(arr)

    index_dic = {}
    for i, num in enumerate(answer):
        index_dic[num] = i

    cnt = 0
    for i in range(n-1):
        com = abs(index_dic[arr[i]] - index_dic[arr[i+1]])
        if com == 1:
            continue
        cnt += 1

    return cnt

print(solution(N, rib))