def solution(A, B):
    answer = 0
    if min(A) >= max(B):
        return answer
    A.sort()
    B.sort(reverse=True)
    for a in A:
        while B:
            b = B.pop()
            if b > a:
                answer += 1
                break
    return answer