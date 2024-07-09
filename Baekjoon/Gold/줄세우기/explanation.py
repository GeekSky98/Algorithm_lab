import sys

n = int(sys.stdin.readline())
kids = [int(sys.stdin.readline()) for _ in range(n)]

def solution(n, kids):
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if kids[i] > kids[j]:
                dp[i] = max(dp[i], dp[j]+1)

    return n - max(dp)

print(solution(n, kids))