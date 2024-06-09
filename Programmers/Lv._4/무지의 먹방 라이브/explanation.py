import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    food_heap = []
    for i, time in enumerate(food_times):
        heapq.heappush(food_heap, (time, i + 1))

    total_time = 0
    previous_time = 0
    length = len(food_times)

    while total_time + ((food_heap[0][0] - previous_time) * length) <= k:
        now = heapq.heappop(food_heap)[0]
        total_time += (now - previous_time) * length
        length -= 1
        previous_time = now

    result = sorted(food_heap, key=lambda x: x[1])
    return result[(k - total_time) % length][1]