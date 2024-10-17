n, m = map(int, input().split())
bags = [tuple(map(int, input().split())) for _ in range(n)]

item_list = []

for w, p, a in bags:

    i = 1
    while a > 0:
        take = min(i, a)
        item_list.append((w*take, p*take))
        a -= take
        i *= 2

dp = [0] * (m+1)

for weight, price in item_list:
    for i in range(m, weight-1, -1):
        dp[i] = max(dp[i], dp[i-weight]+price)

print(dp[m])