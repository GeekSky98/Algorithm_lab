def solution(n):
    return str(int(''.join(sorted(list(map(str, n)), key=lambda x: x*3, reverse=True))))