import sys

bag, n = map(int, sys.stdin.readline().split())
jew = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

max_price = 0
for weight, price in sorted(jew, key=lambda x: x[1], reverse=True):
    if weight < bag:
        max_price += weight * price
        bag -= weight
    else:
        max_price += price * bag
        break

print(max_price)