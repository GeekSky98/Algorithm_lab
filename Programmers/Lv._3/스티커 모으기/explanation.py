def solution(s):
    n = len(s)
    if n == 1:
        return s[0]

    dp1 = [0] * n
    dp2 = [0] * n

    dp1[0] = s[0]
    dp1[1] = dp1[0]
    for i in range(2, n-1):
        dp1[i] = max(dp1[i-1], dp1[i-2]+s[i])

    dp2[0] = 0
    dp2[1] = s[1]
    for j in range(2, n):
        dp2[j] = max(dp2[j-1], dp2[j-2]+s[j])

    return max(dp1[n-2], dp2[n-1])