n=int(input())
def d(a):
    s=[]
    for i in a:
        if i=='(':
            s.append(i)
        else:
            if s:
                s.pop()
            else:
                return 'NO'
    return 'NO' if s else 'YES'
for _ in range(n):
    print(d(input().strip()))