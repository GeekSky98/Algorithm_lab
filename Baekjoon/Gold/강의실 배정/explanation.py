import sys
n = int(sys.stdin.readline())
class_start = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(n)], key=lambda x: x[0])
class_end = sorted(class_start, key=lambda x: x[1])
start_idx = end_idx = current_room = max_room = 0
while start_idx < n:
    if class_start[start_idx][0] < class_end[end_idx][1]:
        current_room += 1
        max_room = max(max_room, current_room)
        start_idx += 1
    else:
        current_room -= 1
        end_idx += 1

print(max_room)