def solution(a, b):
    a.sort()
    b.sort()
    for i in range(len(b)):
        if a[i] != b[i]:
            return a[i]
    return a[-1]