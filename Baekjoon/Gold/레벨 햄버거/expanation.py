import sys
n, x = map(int, sys.stdin.readline().split())

def solution(n, x):
    dp = [0] * (n + 1)
    dp_patty = [0] * (n + 1)
    dp[0] = 1
    dp_patty[0] = 1

    for i in range(1, n + 1):
        dp[i] = 2 * (dp[i-1]) + 3
        dp_patty[i] = 2 * (dp_patty[i-1]) + 1

    eaten = 0
    level = n
    while x > 0:
        if level == 0:
            eaten += 1
            break
        elif x == 1:
            break
        elif x <= 1 + dp[level - 1]:
            x -= 1
            level -= 1
        elif x == 2 + dp[level - 1]:
            eaten += dp_patty[level - 1] + 1
            break
        elif x <= 2 + 2 * dp[level - 1]:
            eaten += dp_patty[level - 1] + 1
            x -= 2 + dp[level - 1]
            level -= 1
        else:
            eaten += 2 * (dp_patty[level - 1]) + 1
            break

    return eaten

print(solution(n, x))