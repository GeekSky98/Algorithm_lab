from itertools import permutations

def is_prime(num):
    if num < 2:
        return False
    if num < 4:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5, int(num**0.5)+1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True

def solution(numbers):
    numbers = list(numbers)
    all_num = set()
    for i in range(1, len(numbers) + 1):
        for sub in permutations(numbers, i):
            all_num.add(int("".join(sub)))

    answer = 0
    for num in all_num:
        if is_prime(num):
            answer += 1

    return answer