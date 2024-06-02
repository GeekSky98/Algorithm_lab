def solution(s):
    r = len(s)
    for i in range(1, len(s)//2+1):
        l = [s[j:j+i] for j in range(0, len(s), i)]
        t, c = 1, []
        for a in range(1, len(l)):
            if l[a]==l[a-1]:
                t+=1
            else:
                c.append(f'{t}{l[a-1]}' if t>1 else l[a-1])
                t=1
        c.append(f'{t}{l[-1]}' if t>1 else l[-1])
        r=min(r,len(''.join(c)))
    return r