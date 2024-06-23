import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
farm = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
friends = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]

visited = [[False] * n for _ in range(n)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

start = ()
queue = deque([])

