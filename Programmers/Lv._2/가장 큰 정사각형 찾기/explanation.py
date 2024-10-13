def solution(board):
    n = len(board)
    m = len(board[0])
    dp = [[0] * m for _ in range(n)]

    max_len = 0

    for i in range(m):
        dp[0][i] = board[0][i]
        max_len = max(dp[0][i], board[0][i])  # 0 방지

    for i in range(n):
        dp[i][0] = board[i][0]
        max_len = max(dp[i][0], board[i][0])

    for i in range(1, n):
        for j in range(m):
            if board[i][j] == 1:
                dp[i][j] = min(dp[i-1][j],dp[i][j-1], dp[i-1][j-1]) + 1
                max_len = max(max_len, dp[i][j])

    return max_len ** 2