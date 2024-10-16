n = int(input())
arr = [list(input().strip()) for _ in range(n)]

def check_xy(arr, n):
    max_cnt = 1
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if arr[i][j] == arr[i][j-1]:
                cnt += 1
                max_cnt = max(max_cnt, cnt)
            else:
                cnt = 1

    for j in range(n):
        cnt = 1
        for i in range(1, n):
            if arr[i][j] == arr[i-1][j]:
                cnt += 1
                max_cnt = max(max_cnt, cnt)
            else:
                cnt = 1

    return max_cnt


max_value = 0
for i in range(n):
    for j in range(n):
        if j < n-1 and  arr[i][j] != arr[i][j+1]:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            max_value = max(max_value, check_xy(arr, n))
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]

        if i < n-1 and arr[i][j] != arr[i+1][j]:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            max_value = max(max_value, check_xy(arr, n))
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]

print(max_value)