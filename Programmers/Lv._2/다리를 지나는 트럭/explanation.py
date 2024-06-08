from collections import deque
def solution(bridge_length, weight, truck_weights):
    truck = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    time = now_w = 0

    while bridge:
        time += 1
        now_w -= bridge.popleft()

        if truck:
            if now_w + truck[0] <= weight:
                target = truck.popleft()
                bridge.append(target)
                now_w += target
            else:
                bridge.append(0)

    return time