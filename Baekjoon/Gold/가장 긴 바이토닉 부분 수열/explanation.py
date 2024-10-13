n = int(input())
data = list(map(int, input().split()))

def lis(d):
    dp = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if d[i] > d[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp

data_lis = lis(data)
data_lis_reverse = lis(data[::-1])[::-1]

max_value = 0
for i in range(n):
    max_value = max(max_value, data_lis[i] + data_lis_reverse[i] - 1)

print(max_value)