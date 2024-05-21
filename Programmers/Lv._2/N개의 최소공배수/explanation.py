def solution(arr):
    max_num = max(arr)
    arr_len = len(arr)
    target = 1
    while True:
        index, target_num = 0, max_num * target
        for now in arr:
            if target_num % now == 0:
                index += 1
        if index == arr_len:
            return target_num
        target += 1