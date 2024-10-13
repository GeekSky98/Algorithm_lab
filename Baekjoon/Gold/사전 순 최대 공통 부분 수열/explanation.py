A = int(input())
a = list(map(int, input().split()))
B = int(input())
b = list(map(int, input().split()))

dp = [[0] * (A + 1) for _ in range(B + 1)]
for i in range(1, B + 1):
    for j in range(1, A + 1):
        if b[i - 1] == a[j - 1]:
            dp[i][j] = dp[i-1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

lcs = []
i, j = B, A
while i > 0 and j > 0:
    if b[i - 1] == a[j - 1]:
        lcs.append(b[i-1])
        i -= 1
        j -= 1
    else:
        if dp[i-1][j] >= dp[i][j-1]:
            i -= 1
        else:
            j -= 1

# 굳이 LCS로 풀 필요가 없음.
A = int(input())
a = list(map(int, input().split()))
B = int(input())
b = list(map(int, input().split()))

same = set(a).intersection(b)
same = sorted(list(same), reverse=True)

answer = []
a_index, b_index = 0, 0
while a_index < A and b_index < B:
    flag = False
    for i in same:
        a_flag = b_flag = -1
        for a_i in range(a_index, A):
            if a[a_i] == i:
                a_flag = a_i
                break
        for b_i in range(b_index, B):
            if b[b_i] == i:
                b_flag = b_i
                break
        if a_flag != -1 and b_flag != -1:  # 인덱스가 0일 수도 있으니, 0으로 해서 and 연산으로 하는 건 불가.
            answer.append(i)
            a_index, b_index = a_flag + 1, b_flag +1
            flag = True
            break
    if not flag:
        break

print(len(answer))
print(" ".join(map(str, answer)))