def solution(order):
    stack, current, index, length = [], 1, 0, len(order)
    while index < length:
        if current == order[index]:
            index += 1
            current += 1
        elif stack and stack[-1] == order[index]:
            stack.pop()
            index += 1
        elif current <= length:
            stack.append(current)
            current += 1
        else:
            break
    return index