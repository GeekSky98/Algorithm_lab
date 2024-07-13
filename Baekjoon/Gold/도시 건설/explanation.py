import sys
from collections import defaultdict

n, m = map(int, sys.stdin.readline().split())
edge = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

graph = defaultdict(list)
for start, end, cost in edge:
    