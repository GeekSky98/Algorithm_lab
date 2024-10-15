def solution(n):
    prime = [1] * (n + 1)
    prime[0] = prime[1] = 0

    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(i ** 2, n + 1, i):
                prime[j] = 0

    return sum(prime)