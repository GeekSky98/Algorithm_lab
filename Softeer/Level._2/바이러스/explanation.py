import sys
k, p, n = map(int, sys.stdin.readline().split())
MOD = 1000000007
print((k * pow(p, n, MOD))%MOD)