from math import ceil
def solution(n,a,b):
    match = 1
    while True:
        a = ceil(a / 2)
        b = ceil(b / 2)

        if a == b:
            return match

        match += 1

print(solution(8,4,7))