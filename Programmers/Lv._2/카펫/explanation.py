def solution(brown, yellow):
    div = 0
    while True:
        div += 1
        a, b = divmod(yellow, div)
        if b == 0:
            if (a * 2) + (div * 2) + 4 == brown:
                return [max(a+2, div+2), min(a+2, div+2)]