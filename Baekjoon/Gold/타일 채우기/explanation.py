import sys
n = int(input())

def solution(n):
    if n % 2 != 0:
        print(0)
        return
    dp = [0]*(n+1)
    dp[0] = 1
    dp[2] = 3

    for i in range(4, n+1, 2):
        dp[i] = dp[i-2] * 3


    이거 너무 어렵다..