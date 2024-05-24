def solution(n, k):
    s = []
    for t in n:
        while s and s[-1] < t and k > 0:
            s.pop()
            k-=1
        s.append(t)
    return ''.join(s) if k == 0 else ''.join(s)[:-k]