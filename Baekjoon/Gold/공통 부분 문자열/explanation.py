a = input().strip()
b = input().strip()
a_len = len(a)
b_len = len(b)

dp = [0] * (b_len + 1)
max_len = 0
for i in range(1, a_len+1):
    dp2 = [0] * (a_len + 1)
    for j in range(1, b_len+1):
        if a[i-1] == b[j-1]:
            dp2[j] = dp[j-1] + 1
            max_len = max(max_len, dp2[j])
    dp = dp2

print(max_len)