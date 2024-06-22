def solution(n, s):
    if n > s:
        return [-1]
    a, b = divmod(s, n)
    answer = [a]*n
    for i in range(b):
        answer[-i-1] += 1
    return answer