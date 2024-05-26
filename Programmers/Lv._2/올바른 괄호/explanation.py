def solution(s):
    t = 0
    for a in list(s):
        t += 1 if a == '(' else -1
        if t < 0:
            return False
    return True if t == 0 else False