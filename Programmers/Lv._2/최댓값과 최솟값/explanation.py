def solution(s):
    t = sorted([int(i) for i in s.split(' ')])
    return f'{t[0]} {t[-1]}'