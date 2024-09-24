n = int(input())

cnt = [0] * 10
target = 1

while n >= target:
    low = n - (n // target) * target
    high = (n // target) // 10
    current = (n // target) % 10

    for i in range(10):
        cnt[i] += high * target

    for i in range(current):
        cnt[i] += target

    cnt[current] += low + 1

    cnt[0] -= target
    target *= 10

print(" ".join(map(str,cnt)))