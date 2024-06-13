import sys
from heapq import heappop, heappush

n = int(sys.stdin.readline())
class_list = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

current_room = index = current_time = max_room = 0
class_list.sort(key=lambda x: x[1])
heap = []
while index < n:
    current_time = class_list[index][1]
    while heap and heap[0] <= current_time:
        heappop(heap)
        current_room -= 1

    heappush(heap, class_list[index][2])
    current_room += 1
    max_room = max(max_room, current_room)
    index += 1

print(max_room)