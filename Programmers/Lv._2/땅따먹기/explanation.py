def solution(land):
    arr_len = len(land)
    dp = [[0] * 4 for _ in range(arr_len)]
    dp[0] = land[0]
    for i in range(1, arr_len):
        for j in range(4):
            if j == 0:
                dp[i][j] = max(dp[i-1][1], dp[i-1][2], dp[i-1][3]) + land[i][j]
            elif j == 1:
                dp[i][j] = max(dp[i-1][0], dp[i-1][2], dp[i-1][3]) + land[i][j]
            elif j == 2:
                dp[i][j] = max(dp[i-1][0], dp[i-1][1], dp[i-1][3]) + land[i][j]
            else:
                dp[i][j] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2]) + land[i][j]

    return max(dp[-1])