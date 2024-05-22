import sys
n, x, y = map(int, sys.stdin.readline().split())

def z_detect(n, x, y):
    answer = 0
    while n > 0:
        n -= 1
        n_2 = 2 ** n

        if x < n_2 and y < n_2:
            continue
        elif x < n_2 and y >= n_2:
            answer += 2 ** (2 * n)
            y -= n_2
        elif x >= n_2 and y < n_2:
            answer += 2 * (2 ** (2 * n))
            x -= n_2
        elif x >= n_2 and y >= n_2:
            answer += 3 * (2 ** (2 * n))
            x -= n_2
            y -= n_2

    return answer

print(z_detect(n,x,y))