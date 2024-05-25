def solution(storey):
    answer = 0
    while storey:
        least, storey = storey % 10, storey // 10
        if (least == 5 and storey % 10 > 4) or (least > 5):
            storey += 1; answer += 10 - least; continue
        answer += least
    return answer