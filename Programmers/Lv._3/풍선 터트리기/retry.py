def solution(a):
    left, right = [a[0]], [a[-1]]
    for i in range(1, len(a)):
        left.append(min(left[-1], a[i]))
    for i in range(len(a)-2, -1, -1):
        right.append(min(right[-1], a[i]))
    right = right[::-1]
    answer = 2
    for i in range(1, len(a)-1):
        if left[i-1] < a[i] and right[i+1] < a[i]:
            continue
        answer += 1
    return answer