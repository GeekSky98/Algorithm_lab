def solution(numbers):
    stack = []
    numbers_idx = [(i, j) for i, j in enumerate(numbers)]
    answer = [-1] * len(numbers)
    for idx, num in numbers_idx:
        while stack and numbers[stack[-1]] < num:
            answer[stack.pop()] = num
        stack.append(idx)

    return answer