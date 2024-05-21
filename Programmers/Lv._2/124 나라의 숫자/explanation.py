def solution(n):
    answer = ''
    while n > 0:
        n -= 1
        num = n % 3
        if num == 0:
            answer = '1' + answer
        elif num == 1:
            answer = '2' + answer
        else:
            answer = '4' + answer
        n //= 3
    return answer