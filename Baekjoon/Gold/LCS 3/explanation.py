import sys

str_1 = input().strip()
str_2 = input().strip()
str_3 = input().strip()

str_1_len, str_2_len, str_3_len = len(str_1), len(str_2), len(str_3)

dp = [[[0] * (str_3_len + 1) for _ in range(str_2_len + 1)] for _ in range(str_1_len + 1)]

for i in range(1, str_1_len +1):
    for j in range(1, str_2_len + 1):
        for k in range(1, str_3_len + 1):
            if str_1[i - 1] == str_2[j - 1] == str_3[k - 1]:
                dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
            else:
                dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

print(dp[-1][-1][-1])