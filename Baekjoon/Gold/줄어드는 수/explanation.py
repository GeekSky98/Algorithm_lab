from itertools import combinations

def solution(N):
    decreasing_numbers = []

    for length in range(1, 11):
        for comb in combinations(range(10), length):
            num = int(''.join(map(str, sorted(comb, reverse=True))))
            decreasing_numbers.append(num)

    decreasing_numbers.sort()

    if N <= len(decreasing_numbers):
        return decreasing_numbers[N - 1]
    else:
        return -1

N = int(input().strip())
print(solution(N))