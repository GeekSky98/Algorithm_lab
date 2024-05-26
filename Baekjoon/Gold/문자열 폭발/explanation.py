import sys
target = sys.stdin.readline().rstrip()
boom = list(sys.stdin.readline().rstrip())
last_char, boom_len = boom[-1], len(boom)
stack = []

for char in target:
    stack.append(char)
    if char == last_char:
        if stack[-boom_len:] == boom:
            for _ in range(boom_len):
                stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")