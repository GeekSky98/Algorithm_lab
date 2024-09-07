import sys
s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()

while len(t) > len(s):
    if t[-1] == "A":
        t = t[:-1]
    elif t[-1] == "B":
        t = t[:-1]
        t = t[::-1]
    else:
        break

print(1 if s == t else 0)