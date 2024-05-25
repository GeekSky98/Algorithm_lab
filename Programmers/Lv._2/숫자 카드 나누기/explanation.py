def gcd(a, b):
    r = b % a
    if r == 0:
        return a
    return gcd(r, a)

def solution(arrA, arrB):
    answer = 0
    arr_reverse = [arrB, arrA]
    for index, arr_now in enumerate([arrA, arrB]):
        temp_num = arr_now[0]
        for num in arr_now:
            temp_num = gcd(temp_num, num)
        result = temp_num
        for target in arr_reverse[index]:
            if target % temp_num == 0:
                result = temp_num // gcd(target, temp_num)
        answer = max(answer, result)

    return 0 if answer == 1 else answer