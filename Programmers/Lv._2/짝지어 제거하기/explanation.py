def solution(s):
    t=[]
    for i in s:
        if t and t[-1]==i:
            t.pop()
        else:
            t.append(i)
    return 0 if t else 1