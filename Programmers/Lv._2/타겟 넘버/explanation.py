def solution(n,t):
    l=len(n)
    def f(i,s):
        if i==l:return 1 if s==t else 0
        return f(i+1,s+n[i])+f(i+1,s-n[i])
    return f(0,0)