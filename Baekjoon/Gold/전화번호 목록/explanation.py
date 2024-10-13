def solution(arr, n):
    arr.sort()
    for i in range(1, n):
        if arr[i].startswith(arr[i-1]):
            return 'NO'
    return 'YES'

case = int(input())
for _ in range(case):
    n = int(input().strip())
    arr = [str(input().strip()) for _ in range(n)]
    print(solution(arr, n))