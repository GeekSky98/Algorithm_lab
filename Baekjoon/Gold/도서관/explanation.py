import sys
n, m = map(int, sys.stdin.readline().split())
location = list(map(int, sys.stdin.readline().split()))

left, right = [], []
for l in location:
    if l < 0:
        left.append(-l)
    else:
        right.append(l)

left.sort(reverse=True)
right.sort(reverse=True)

def distance(target):
    cost = 0
    for i in range(0, len(target), m):
        cost += target[i] * 2
    return cost

if left and right:
    print(distance(left) + distance(right) - max(left[0], right[0]))
elif left:
    print(distance(left) - left[0])
elif right:
    print(distance(right) - right[0])