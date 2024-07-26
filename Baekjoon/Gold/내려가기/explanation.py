import sys

N = int(sys.stdin.readline())
BOARD = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def solution(n, board):
    max_dp = [[0] * n for _ in range(3)]
    min_dp = [[0] * n for _ in range(3)]
    for i, num in enumerate(board[0]):
        max_dp[0][i] = num
        min_dp[0][i] = num

    for i in range(1, n):
        for j in range(n):
            if j == 0:
                max_dp[i][j] = max(max_dp[i-1][j], max_dp[i-1][j+1]) + board[i][j]
                min_dp[i][j] = min(min_dp[i-1][j], min_dp[i-1][j+1]) + board[i][j]
            elif j == n-1:
                max_dp[i][j] = max(max_dp[i-1][j-1], max_dp[i-1][j]) + board[i][j]
                min_dp[i][j] = min(min_dp[i-1][j-1], min_dp[i-1][j]) + board[i][j]
            else:
                max_dp[i][j] = max(max_dp[i-1][j-1], max_dp[i-1][j], max_dp[i-1][j+1]) + board[i][j]
                min_dp[i][j] = min(min_dp[i-1][j-1], min_dp[i-1][j], min_dp[i-1][j+1]) + board[i][j]

    return max(max_dp[n-1]), min(min_dp[n-1])

max_v, min_v = solution(N, BOARD)
print(max_v, min_v)
##### Try1: 메모리초과... 메모리 제한이 4mb다..



import sys
n = int(sys.stdin.readline())
b = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
m1=m2=m3=n1=n2=n3=0
for i in range(1,n):
    m1, m2, m3 = max(m1, m2) + b[i][0], max(m1, m2, m3) + b[i][1], max(m2, m3) + b[i][2]
    n1, n2, n3 = min(n1, n2) + b[i][0], min(n1, n2, n3) + b[i][1], min(n2, n3) + b[i][2]
print(max(m1,m2,m3),min(n1,n2,n3))
##### Try2: 배열을 써도 메모리 초과...



import sys
n=int(input())
a=list(map(int, sys.stdin.readline().split()))
d,p=a,a
for _ in range(n-1):
    a,b,c=map(int, sys.stdin.readline().split())
    d=[max(d[0],d[1])+a,max(d[0],d[1],d[2])+b,max(d[1],d[2])+c]
    p=[min(p[0],p[1])+a,min(p[0],p[1],p[2])+b,min(p[1],p[2])+c]
print(max(d),min(p))
#####성공..