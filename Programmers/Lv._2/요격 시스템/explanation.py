def solution(a):
    t = z = 0
    for b in sorted(a, key=lambda x: x[1]):
        if b[0] >= t: t = b[1]; z += 1
    return z