import sys
from collections import deque

m, n, k = map(int, sys.stdin.readline().split())
recipe = list(map(int, sys.stdin.readline().split()))
menu = list(map(int, sys.stdin.readline().split()))

queue = deque(menu)
stack = []
last_str = recipe[-1]
recipe_len = len(recipe)
secret_flag = False

while queue:
    now = queue.popleft()
    stack.append(now)
    if now == last_str:
        if stack[-recipe_len:] == recipe:
            secret_flag = True
            break

print("secret" if secret_flag else "normal")