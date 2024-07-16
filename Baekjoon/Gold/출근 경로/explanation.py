import sys

w, h = map(int, sys.stdin.readline().split())

def solution(w, h):
    MOD = 100000
    dp = [[[0, 0] for _ in range(h+1)] for _ in range(w+1)]
    dp[1][1][0] = dp[1][1][1] = 1

    for i in range(1, w + 1):
        for j in range(1, h + 1):
            if i > 1:
                dp[i][j][0] += (dp[i-1][j][1] % MOD)
            if j > 1:
                dp[i][j][1] += (dp[i][j-1][0] % MOD)

    return (dp[w][h][0] + dp[w][h][1]) % MOD

print(solution(w, h))
## 실패