n = int(input())
commands = [tuple(input().split()) for _ in range(n)]

stack = []
s_len = 0
for c in commands:
    now = c[0]
    if now == 'push':
        stack.append(int(c[1]))
        s_len += 1
    elif now == 'pop':
        if s_len > 0:
            print(stack.pop())
            s_len -= 1
        else:
            print(-1)
    elif now == 'size':
        print(s_len)
    elif now == 'empty':
        print(1 if s_len == 0 else 0)
    elif now == 'top':
        print(stack[-1] if s_len > 0 else -1)