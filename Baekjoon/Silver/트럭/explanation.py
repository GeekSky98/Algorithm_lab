from collections import deque

n, w, l = map(int, input().split())
truck = deque(list(map(int, input().split())))

queue = deque([0] * w)
current_weight = 0
time = 0
while queue:
    time += 1
    current_weight -= queue.popleft()
    if truck:
        if current_weight + truck[0] <= l:
            current_weight += truck[0]
            queue.append(truck.popleft())
        else:
            queue.append(0)

print(time)