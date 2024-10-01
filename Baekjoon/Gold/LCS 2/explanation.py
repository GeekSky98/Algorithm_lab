import sys

str_1 = input().strip()
str_2 = input().strip()

str_1_len, str_2_len = len(str_1), len(str_2)

dp = [[0] * (str_2_len + 1) for _ in range(str_1_len + 1)]

for i in range(1, str_1_len +1):
    for j in range(1, str_2_len + 1):
        if str_1[i - 1] == str_2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])

i, j = str_1_len, str_2_len
answer = []
while i > 0 and j > 0:
    if str_1[i - 1] == str_2[j - 1]:
        answer.append(str_1[i - 1])
        i -= 1
        j -= 1
    elif dp[i - 1][j] > dp[i][j - 1]:
        i -= 1
    else:
        j -= 1

print("".join(reversed(answer)))