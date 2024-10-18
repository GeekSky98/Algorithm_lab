def solution(number, k):
    stack = []
    for i in number:
        while stack and k > 0 and i > stack[-1]:
            stack.pop()
            k -= 1
        stack.append(i)

    return ''.join(stack) if k == 0 else ''.join(stack[:-k])