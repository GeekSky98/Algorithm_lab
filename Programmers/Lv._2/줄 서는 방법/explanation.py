from math import factorial
def solution(n, k):
    people, answer = list(range(1, n+1)), []
    k -= 1
    while n > 0:
        n -= 1
        fac = factorial(n)
        index, k = divmod(k, fac)
        answer.append(people.pop(index))
    return answer