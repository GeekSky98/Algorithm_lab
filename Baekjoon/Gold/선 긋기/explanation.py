import sys
n = int(sys.stdin.readline())
lines = sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(n)], key=lambda x: (x[0], x[1]))

left, right = lines.pop(0)
answer = right-left
for start, end in lines:
    if start > right:
        answer += end - start
        left, right = start, end
    else:
        if end - right > 0:
            answer += end - right
            right = end

print(answer)