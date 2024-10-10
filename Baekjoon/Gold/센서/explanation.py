import sys
n = int(input())
k = int(input())
sensor = list(map(int, sys.stdin.readline().split()))

sensor.sort()
diff = []
for i in range(1, n):
    diff.append(sensor[i] - sensor[i - 1])

diff.sort(reverse=True)
print(sum(diff[k-1:]))