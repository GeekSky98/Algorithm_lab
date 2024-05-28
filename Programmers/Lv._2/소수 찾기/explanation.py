from itertools import permutations
def is_prime(num):
    if num < 2:
        return False
    if num <= 3:
        return True
    if num % 2 ==0 or num % 3 == 0:
        return False
    for i in range(5, int(num**0.5) + 1, 6):
        if num % i == 0 or num % (i+2) == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    len_num = len(numbers)
    all_num = set()
    for i in range(1, len_num+1):
        for j in permutations(numbers, i):
            all_num.add(int(''.join(j)))

    for num in all_num:
        if is_prime(num):
            answer += 1
    return answer