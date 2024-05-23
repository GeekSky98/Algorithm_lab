def count_alarm(h, m, s):
    itr = (h*60+m)*2-h-1-(2 * (h >= 12))
    ht, mt, st = (30*(h%12))+0.5*m+(1/120*s), 6*m+(1/60*s), 6*s
    return itr+(ht<=st)+(mt<=st)

def solution(h1, m1, s1, h2, m2, s2):
    a, b = count_alarm(h2, m2, s2), count_alarm(h1, m1, s1)
    return a-b+((h1%12==0) and m1==s1==0)