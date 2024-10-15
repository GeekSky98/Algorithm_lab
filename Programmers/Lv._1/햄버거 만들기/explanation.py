def solution(ingredient):
    answer = 0
    total = [1, 2, 3, 1]
    total_len = len(total)
    stack = []
    for i in ingredient:
        stack.append(i)
        if i == 1:
            if stack[-total_len:] == total:
                answer += 1
                for i in range(total_len):
                    stack.pop()

    return answer

print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))