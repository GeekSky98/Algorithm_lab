import sys
n = int(sys.stdin.readline())

result = ""
while n > 0:
    n, div = divmod(n-1, 2)
    if div == 0:
        result = "4" + result
    else:
        result = "7" + result

print(int(result))