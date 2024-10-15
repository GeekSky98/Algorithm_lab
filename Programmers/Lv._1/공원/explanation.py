def solution(mats, park):
    x_len, y_len = len(park), len(park[0])
    dp = [[0] * y_len for _ in range(x_len)]

    max_len = 0
    for i in range(x_len):
        for j in range(y_len):
            if park[i][j] == '-1':
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
            max_len = max(max_len, dp[i][j])

    for i in (sorted(mats, reverse=True)):
        if i <= max_len:
            return i

    return -1