import sys

N = int(sys.stdin.readline())
BOARD = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def solution(n, board):
    dp = [[0]*n for _ in range(n)]

    dp[0][0] = 1

    for i in range(n):
        for j in range(n):
            if i == n-1 and j == n-1:
                break
            num = board[i][j]
            if num == 0:
                continue
            if i + num < n:
                dp[i+num][j] += dp[i][j]
            if j + num < n:
                dp[i][j+num] += dp[i][j]

    return dp[-1][-1]

print(solution(N, BOARD))