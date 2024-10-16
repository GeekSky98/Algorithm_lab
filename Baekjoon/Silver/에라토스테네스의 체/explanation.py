n, k = map(int, input().split())

def era(num, k):
    prime = [1] * (num + 1)
    cnt = 0
    for i in range(2, num+1):
        if prime[i]:
            for j in range(i, num + 1, i):
                if prime[j]:
                    prime[j] = 0
                    cnt += 1
                    if cnt == k:
                        return j

print(era(n, k))