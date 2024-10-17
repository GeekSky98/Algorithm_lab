from heapq import heappush, heappop

n = int(input())
data = list(map(int, input().split()))
data = [(d, i)for i, d in enumerate(data)]

stack = []
heappush(stack, data[0])

answer = [-1] * n

for i in range(1, len(data)):
    target, target_idx = data[i]
    while stack and stack[0][0] < target:
        _, low_idx = heappop(stack)
        answer[low_idx] = target

    heappush(stack, (target, target_idx))

print(" ".join(map(str, answer)))

# ------------ 그냥 stack으로 한다면?

n = int(input())
data = list(map(int, input().split()))
stack = []
answer = [-1] * n
for i in range(n):
    while stack and data[stack[-1]] < data[i]:
        answer[stack.pop()] = data[i]
    stack.append(i)
print(" ".join(map(str, answer)))