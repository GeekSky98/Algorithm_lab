def solution(begin, end):  # 최대 공약수 문제
    answer = []

    for i in range(begin, end+1):
        if i == 1:
            answer.append(0)
            continue
        if i % 2 == 0 and i // 2 <= 10000000:
            answer.append(i // 2)
        else:
            divisor = 1
            for j in range(2, int(i**0.5)+1):
                if i % j == 0:
                    if i//j <= 10000000:
                        divisor = max(divisor, i//j)
                    if j <= 10000000:
                        divisor = max(divisor, j)
            answer.append(divisor)

    return answer