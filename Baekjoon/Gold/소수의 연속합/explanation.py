import sys

n = int(input())

dp = [True] * (n + 1)
dp[0] = dp[1] = False
for i in range(2, int(n ** 0.5) + 1):
    if dp[i]:
        for j in range(i * i, n + 1, i):
            dp[j] = False

data = [i for i in range(2, n + 1) if dp[i]]

left = right = current = cnt = 0

while right <= len(data):
    if current == n:
        cnt += 1
        current -= data[left]
        left += 1
    elif current < n:
        if right < len(data):
            current += data[right]
        right += 1
    else:
        current -= data[left]
        left += 1

print(cnt)