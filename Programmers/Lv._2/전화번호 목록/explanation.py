def solution(p):
    p.sort()
    for i in range(len(p)-1):
        if p[i+1].startswith(p[i]):
            return False
    return True