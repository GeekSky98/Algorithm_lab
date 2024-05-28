def solution(numbers):
    answer, stack = [-1]*len(numbers), []
    for index, num in enumerate(numbers):
        while stack and numbers[stack[-1]] < num:
            answer[stack.pop()] = num
        stack.append(index)
    return answer